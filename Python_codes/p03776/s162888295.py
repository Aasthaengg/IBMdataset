import math
def combi(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n,a,b = map(int,input().split())
l = sorted(list(map(int,input().split())),reverse = True)
n_max = l.count(max(l))
ans=0
if n_max>a:
    for i in range(a,min(b+1,n_max+1)):
        ans+=combi(n_max,i)
    print(max(l))
    print(ans)
    exit()
n_min = l.count(l[a-1])
i_min = l.index(l[a-1])
k = a-i_min
ans+=combi(n_min,k)
print(sum(l[:a])/a)
print(ans)