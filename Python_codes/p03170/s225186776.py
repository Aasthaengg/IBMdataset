n,k = map(int, input().split())
a = list(map(int, input().split()))
ans=[-1]*(k+1)
ans[0]=False # lose

for i in range(k+1):
    iswin = False
    for num in a:
        if (i-num >=0) and (not ans[i-num]):
            iswin=True
    ans[i]=iswin

if ans[-1]:
    print("First")
else:
    print("Second")