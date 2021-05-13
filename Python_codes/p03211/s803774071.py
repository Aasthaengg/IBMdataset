S = input()
N = len(S)

ans = 999
for i in range(0,N-2):
  n = int(S[i:i+3])
  ans = min(ans, abs(n - 753))
  #print(n)
  
print(ans)