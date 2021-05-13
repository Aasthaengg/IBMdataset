n=int(input())
p=[int(x) for x in input().rstrip().split()]

now_min=float('inf')
cnt=0
for i in range(n):
  if p[i]<=now_min:
    cnt+=1
    now_min=p[i]
  
print(cnt)

