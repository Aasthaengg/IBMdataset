import math

q = int(input())

def is_prime(a):
    if a == 1:
        return False
    for i in range(2,int(math.sqrt(a)+1)):
        if a%i == 0:
            return False
    else:
        return True

s = [0 for i in range(0,100001)]
for i in range(3,100001,2):
    if is_prime(i) and is_prime((i+1)//2):
        s[i] = 1

s2 = [0 for i in range(0,100001)]
tmp = 0
for i in range(100001):
    tmp += s[i]
    s2[i] = tmp

for i in range(q):
    l,r = map(int,input().split())
    ans = s2[r] - s2[l-1]
    print(ans)


