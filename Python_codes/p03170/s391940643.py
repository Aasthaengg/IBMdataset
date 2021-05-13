n,k = map(int, input().split())
a = list(map(int, input().split()))
ans=[False]*(k+1)
ans[0]=False

for i in range(k+1):
    for num in a:
        if (i-num >=0) and (not ans[i-num]):
            ans[i]=True

if ans[-1]:
    print("First")
else:
    print("Second")