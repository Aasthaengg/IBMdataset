N=int(input())
A = list(map(int,input().split(' ')))
B = list(map(int,input().split(' ')))
a=0
b=0
for i,j in zip(A,B):
    if j-i>=0:
        a += (j-i)//2
    else:
        b += i-j
if a >= b:
    print('Yes')
else:
    print('No')