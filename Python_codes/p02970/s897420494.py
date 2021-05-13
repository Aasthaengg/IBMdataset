#1 2 3 4 5
n,d = map(int,input().split())
ans = n//(2 * d + 1)
if n%(2 * d + 1) == 0:
    print(ans)
else:
    print(ans+1)