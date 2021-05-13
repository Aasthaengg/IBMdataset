import math
N,M= map(int, input().split())
a = list(map(int, input().split()))
A=[0]*N
#２で何回割れるか
for i in range(N):
    num=0
    while a[i]%2==0:
        num+=1
        a[i]=int(a[i]/2)
    A[i]=num

for i in range(N):
    if A[0]==A[i]:
        s=True
    else:
        s=False
        break
if s:
    M=M/(2**(A[i]-1))
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    def lcm(a, b):
        return a * b // gcd (a, b)
    ak=a[0]
    for i in range(N):
        ak=lcm(ak,a[i])
    #print(ak)
    if ak>M:
        print(0)
    else:
        print(math.ceil(int(M/ak)/2))
else:
    print(0)