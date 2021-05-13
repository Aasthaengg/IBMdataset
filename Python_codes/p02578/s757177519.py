n=int(input())

row=list(map(int,input().split()))


s=0
for i in range(1,n):
    if row[i-1]>row[i]:
        s+=row[i-1]-row[i]
        row[i]=row[i-1]
print(s)
