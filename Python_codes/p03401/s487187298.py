N=int(input())
A=list(map(int,input().split()))
A.insert(0,0)
A.append(0)

plan=[]
for i in range(N+1):
  plan.append(abs(A[i+1]-A[i]))

total=sum(plan)
for i in range(N):
  ans=total-plan[i]-plan[i+1]+abs(A[i+2]-A[i])
  print(ans)