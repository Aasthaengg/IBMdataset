A,B=input().split()
a=int(A[0])*10+int(A[1])
b=int(B[0])*10+int(B[1])
d=int(A[1])*10+int(A[0])
e=int(B[1])*10+int(B[0])
count_small=0
count_large=0
if a==b:
    for i in range(0,10):
        if a*1000+d+i*100>=int(A) and b*1000+e+i*100<=int(B):
            count_small+=1
    ans=count_small
else:
    for i in range(0,10):
        if a*1000+d+i*100>=int(A):
            count_small+=1
        if b*1000+e+i*100<=int(B):
            count_large+=1
    ans=(b-a-1)*10+count_small+count_large
print(ans)