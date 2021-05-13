def check(n,k,p,T):
    i = 0
    for j in range(k):
        s = 0
        while(s+T[i] <= p):
            s = s+T[i]
            i = i+1
            if (i==n):
                return n
    return i


def solve(n,k,T):
    left =0
    right = 100000 * 10000
    mid = 0
    while (right -left > 1):
        mid = (left + right)//2
        v = check(n,k,mid,T)
        if (v >= n):
            right = mid
        else:
            left = mid
    return right

lis=[]
a = input()
(nn,kk)=list(map(int,a.split()))
for i in range(nn):
    lis.append(int(input()))
ans = solve(nn,kk,lis)
print(ans)