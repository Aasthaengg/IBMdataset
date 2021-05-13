import copy
N=int(input())
a=[int(i) for i in input().split()]
B=copy.deepcopy(a)
A=0
for i in range(N):
    if a[i] < 0:
        a[i]*=-1
    else:
        continue
# print(a)   #2  5  1
# print(B)   #-2 5 -1
q=0
absmax=max(a)
print(2*N-1)
for i in range(N):
    if max(a)==a[i]:
        q=i
        break
if B[q]>=0:
    for i in range(N):
        B[i]+=absmax
        print("{} {}".format(q+1,i+1))
    for j in range(1,N):
        print("{} {}".format(j,j+1))
else:
    for i in range(N):
        B[i]-=absmax
        print("{} {}".format(q+1,i+1))
    for j in range(1,N):
        print("{} {}".format(N-j+1,N-j))