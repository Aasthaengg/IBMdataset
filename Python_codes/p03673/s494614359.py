def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    if n%2 == 0:
        for i in range(n//2):
            ans.append(a[(-i*2)-1])
        for j in range(n//2):
            ans.append(a[(j*2)])
    else:
        for i in range(n//2+1):
            ans.append(a[(-i*2)-1])
        for j in range(n//2):
            ans.append(a[(j*2)+1])
    print(*ans)
resolve()