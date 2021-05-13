N,K = list(map(int,input().split()))
A = list(map(int,input().split()))

l = 0
r = 1000000000

def judge(m):
    k = 0
    for i in range(N):
        if A[i]%m==0:
            k+=A[i]//m-1
        else:
            k+=A[i]//m
    return k<=K

while r-l>1:
    if judge((l+r)//2):
        r = (l+r)//2
    else:
        l = (l+r)//2
print(r)