N=int(input())
H=list(map(int,input().split()))
h=min(H)
count=min(H)
flag=False
while max(H)>=h:
    for i in range(N):
        if flag and H[i]<=h:
            flag=False
            count+=1
        elif flag==False and H[i]>h:
            flag=True
        if i==N-1 and flag:
            count+=1
            flag=False
    h+=1
print(count)
