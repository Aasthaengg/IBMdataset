x=int(input())
n=10**5
import math
def eratosthenes(n):
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]
q=eratosthenes(n)

ans=[0]*(10**5+1)
for i in range(10**5):
    ans[i+1]=ans[i]+(1 if i+1 in q and (i+1+1)//2 in q else 0 )
for i in range(x):
    l,r = map(int,input().split())	
    print(ans[r]-ans[l-1])