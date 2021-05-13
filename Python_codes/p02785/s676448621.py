N,K = map(int,input().split())
H = list(map(int,input().split()))
H.sort(reverse=True)

cnt = 0
if N <= K:
  cnt = 0
else:
  cnt += sum(H[K:])
  
print(cnt)