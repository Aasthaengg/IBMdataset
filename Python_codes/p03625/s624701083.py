n=int(input())
A=list(map(int,input().split()))
ans1=0
ans2=0
A.sort(reverse=True)
flag = False
for i in range(n-1):
  if flag == True:
    flag = False
    continue
  if i < n-1 and A[i+1] == A[i]:
    flag = True
    if A[i] >= ans1:
      ans2 = ans1
      ans1 = A[i]
    elif A[i] > ans2:
      ans2 =A[i]
print(ans1*ans2)
