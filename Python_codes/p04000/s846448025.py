H,W,N=list(map(int,input().split()))

dic={}
for _ in range(N):
    a,b=list(map(int,input().split()))
    for i in range(-1,2):
        for j in range(-1,2):
            if (a+i)<=1 or b+j<=1 or a+i>=H or b+j >=W:
                continue
            s=(a+i)*W+b+j
            if dic.get(s,0)==0:
                dic[s]=1
            else:
                dic[s]+=1
arr=[0 for i in range(10)]
for v in dic.values():
    arr[v]+=1
arr[0]=(H-2)*(W-2)-sum(arr)
for x in arr:
    print(x)