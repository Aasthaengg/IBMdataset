n,k = map(int,input().split())
a_ls = list(map(int, input().split()))

stroke = k - 1
if k < n:
    rest = n - k
    ans = 1 + -(-rest // stroke)
else:
    ans = 1
print(ans)