N,K =map(int,input().split())
a = list(map(int,input().split()))
a.insert(0,0)

#X学期の評点
for i in range(K+1,N+1):
    iscore = a[i]
    jscore = a[i-1-K+1]
    if iscore > jscore:
        print("Yes")
    else:
        print("No")
