import  math
N,M = map(int,input().split())

def f(M):
    l = []
    for i in range(1,int(math.sqrt(M))+1):
        if M%i==0:
            l.append(i)
    n = len(l)
    for i in range(n):
        j = l[n-1-i]
        if M/j!=j:
            l.append(M//j)
    return l

l = f(M)

for i in range(len(l)):
    n = l[-1-i]
    if M/n >= N:
        ans = n
        break
print(ans)
