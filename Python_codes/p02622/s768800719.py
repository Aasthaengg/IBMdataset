A=input()
B=input()

cnt=0
for i in range(len(A)):
  if A[i]!=B[i]:
    cnt+=1

print(cnt)