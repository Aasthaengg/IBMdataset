N=int(input())
A=list(map(int,input().split()))
A.sort()

B=[A[0]]
for i in range(1,N):
  B.append(B[-1]+A[i])
#print(A)
#print(B)

left=0
for left in range(N-2,-1,-1):
  if B[left]*2>=A[left+1]:
    pass
  else:
    break
else:
  left=-1

num=N-left-1
#print(left)
print(num)

#cnt=0
#for i in range(num,N-1):
#  if A[num]