def f(list,num):
    if list=="E":
        num[0],num[2],num[5],num[3] =num[3],num[0],num[2],num[5]
    elif list=="W":
        num[0],num[2],num[5],num[3] =num[2],num[5],num[3],num[0]
    elif list=="N":
        num[0],num[1],num[5],num[4]=num[1],num[5],num[4],num[0]
    else:
        num[0],num[1],num[5],num[4]=num[4],num[0],num[1],num[5]
L=list(map(int,input().split()))
A=list(str(input()))
for i in range(len(A)):
  f(A[i],L)
print(L[0])
