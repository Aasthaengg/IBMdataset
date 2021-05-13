K,A,B = map(int,input().split())
if B-A-2 <= 0:
  print(K+1)
  exit()

if K-1 < A:
  print(K+1)
  exit()
  
K -= (A-1)
num = K//2
nokori = K%2
#print(K,num,nokori)
ans = A+num*(B-A)+nokori
print(ans)