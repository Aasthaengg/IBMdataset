n=int(input())
k=int(input())
x=list(map(int,input().split()))
ct=0
for i in range(n):
    if (x[i]*2)<(abs(k-x[i])*2):
        ct+=(x[i]*2)
    else:
        ct+=(abs(k-x[i])*2)
print(ct)