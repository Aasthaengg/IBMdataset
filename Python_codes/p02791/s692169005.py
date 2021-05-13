n=int(input())
p=list(map(int,input().split()))
cnt=0
tiny=float('inf')

for i in range(n):
  if tiny>=p[i]:
    cnt+=1
    tiny=p[i]
  else:
    pass
    
print(cnt)