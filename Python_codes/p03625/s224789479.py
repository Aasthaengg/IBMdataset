n=int(input())
lst=sorted(map(int,input().split()),reverse=True)
memory=-1
ans1=-1
for i in range(n):
    if lst[i]==memory:
        if ans1==-1:
            ans1=memory
            memory=-1
        else:
            ans2=memory
            print(ans1*ans2)
            exit()
    else:
        memory=lst[i]

print(0)