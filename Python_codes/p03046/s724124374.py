def MI():
    return map(int,input().split())
def I():
    return int(input())
def LI():
    return [int(i) for i in input().split()]

m,k=MI()

if k>=2**m or (m,k)==(1,1):
    print(-1)
elif (m,k)==(1,0):
    print('0 0 1 1')
else:
    a=[]
    for i in range(2**m):
        if i!=k: a.append(i)
    ans=[k]+a+[k]+a[::-1]
    print(*ans)