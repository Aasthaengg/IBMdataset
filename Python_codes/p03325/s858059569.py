def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in A:
        while i%2 == 0:
            ans += 1
            i = i//2
    print(ans)
resolve()