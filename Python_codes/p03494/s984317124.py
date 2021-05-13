n=int(input())
a=list(map(int,input().split()))
cnt=0
for j in range(10**9):
    for idx,i in enumerate(a):
        if i %2==0:
            a[idx]=i//2
        else:
            print(cnt)
            exit()
    cnt+=1
print(cnt)