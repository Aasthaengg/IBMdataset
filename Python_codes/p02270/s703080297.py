n,k = map(int,input().split())
s = []
for i in range(n):
    s.append(int(input()))

def f(P):
    v = 0
    for j in range(k):
        a = 0
        while(a+s[v]<=P):
            a += s[v]
            v+=1
            if v==n:
                return v
    return v

l = 0
r = 10**9
while l!=r:
    mid = (l+r)//2
    c = f(mid)
    if c>=n:
        r = mid
    else:
        l = mid+1   
print(r)            
