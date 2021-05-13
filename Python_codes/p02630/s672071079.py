def resolve():
    n = int(input())
    a = list(map(int, input().split()))

    q = int(input())
    num_table = [0] * 100010

    for ai in a:
        num_table[ai] += 1

    ans = sum(a)

    for _ in range(q):
        bi, ci = map(int, input().split())
        ans += num_table[bi] * (ci - bi)
        num_table[ci] += num_table[bi]
        num_table[bi] = 0
        print(ans)
        
resolve()