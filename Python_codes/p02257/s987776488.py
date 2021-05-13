def is_prime(x):
    if x==2:
        return 1
    elif x&1==0:
        return 0
    else: return pow(2,x-1,x)==1
N = int(input())
c=0
for i in range(N):
    c+=is_prime(int(input()))
print(c)