n,k = map(int,input().split())
s = 0
for b in range(k+1,n+1):s += n//b*(b-k) + max(n%b-max(k-1,0),0)
print(s)