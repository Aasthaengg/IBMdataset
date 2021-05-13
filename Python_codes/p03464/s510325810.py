K=int(input())
A=list(map(int, input().split()))

mx=2
mn=2
for i in range(K-1,-1,-1):
    a = A[i]
    a_mn = ((mn+a-1)//a)*a
    a_mx = mx - mx%a
    if a_mn > a_mx:
        print(-1)
        exit()
    mn=a_mn
    mx=a_mx+a-1
print("{} {}".format(mn,mx))