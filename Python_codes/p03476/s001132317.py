import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

q=int(input())
l=[]
r=[]
for i in range(q):
    ll,rr=map(int,input().split())
    l.append(ll)
    r.append(rr)

similar=[]
cnt=0
for i in range(10**5+2):
    if i<=2:
        similar.append(0)
    else:
        if is_prime(i)==True and (is_prime((i+1)/2))==True:
            cnt+=1
        similar.append(cnt)

for i in range(q):
    print(similar[r[i]]-similar[l[i]-1])
