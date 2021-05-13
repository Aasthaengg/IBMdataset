N=int(input())
A=[]
for i in range(N):
  A.append(int(input()))
A.sort()
# print(A)

# 想定解で解くしかない
res=0
i=0
while i<N:
  c=A[i]
  f=0
  while i<N and A[i]==c:
    f+=1
    i+=1
  res+=f%2
print(res)