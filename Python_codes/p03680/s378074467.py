N = int(input())
A =[int(input()) for i in range(N)]
l = 1
ans = 0

for n in range(N):
  if l == 2:
    print(ans)
    exit()
  else:
    l = A[l-1]
    ans+=1
    
print(-1)