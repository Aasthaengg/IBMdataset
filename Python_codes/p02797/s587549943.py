n, k, s = map(int, input().split())
if s != 1:
  ans =[s]*k+[s-1]*(n-k) 
else:
  ans =[s]*k+[s+1]*(n-k) 
print(" ".join(list(map(str,ans))))