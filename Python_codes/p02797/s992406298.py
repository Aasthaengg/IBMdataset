n, k, s = map(int, input().split())
 
padding = (s+1)%10**9
ans = [s]* k + [padding]*(n-k)
print(' '.join(map(str, ans)))