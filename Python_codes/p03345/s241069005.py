a,b,c,k = map(int,input().split())
inf = 10**18
ans = a-b
if k%2:ans = -ans
if ans < -inf or ans > inf:print('Unfair')
print(ans)