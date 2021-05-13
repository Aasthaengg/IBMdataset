n, k = map(int, input().split())
if n == 1:
    ans = k
    print(ans)
else:
    ans = k*(k-1)**(n-1)
    print(ans)