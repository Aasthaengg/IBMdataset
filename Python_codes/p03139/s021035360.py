N,A,B=map(int,input().split())
Max=min(A,B)
min=0
if (A+B)>=N:
    min=A+B-N
else:
    min=0
print(Max,min)
