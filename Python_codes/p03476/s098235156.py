import math


def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


N = 100000+1
data = get_sieve_of_eratosthenes(N)
flag = [0]*(N+1)
for i in range(len(data)):
    flag[data[i]]=1

for i in range(N,2,-1):
    if i//2==0 or flag[i]!=1 or flag[(i+1)//2]!=1:
        flag[i]=0
flag[2]=0
for i in range(1,N+1,1):
    flag[i] = flag[i]+flag[i-1]

Q = int(input())

ans = []
for i in range(Q):
    l,r = map(int,input().split())
    ans.append(flag[r]-flag[l-1])

for i in range(len(ans)):
    print(ans[i])