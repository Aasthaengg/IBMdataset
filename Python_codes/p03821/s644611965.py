def solve():
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        A, B = map(int, input().split())
        a.append(A)
        b.append(B)

    ans = b[-1] - a[-1]%b[-1]
    if a[-1]%b[-1] == 0: ans = 0

    for i in range(1, n):
        c = a[-(i+1)]+ans

        if c%b[-(i+1)] == 0: continue

        dis = b[-(i+1)]-c%b[-(i+1)]
        ans += dis

    return ans
    

print(solve())
