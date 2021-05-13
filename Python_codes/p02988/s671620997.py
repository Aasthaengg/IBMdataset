n=int(input())
P=list(map(int,input().split()))
a=[]
for i in range(0,n-2):
    a.append([P[i],P[i+1],P[i+2]])
b=0
for i in range(len(a)):
    if a[i][1]!=min(a[i]) and a[i][1]!=max(a[i]):
        b+=1
print(b)