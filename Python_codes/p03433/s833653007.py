N=int(input())
A=int(input())
n=N//500
a=N-500*n
if a<=A:
    print('Yes')
else:
    print('No')