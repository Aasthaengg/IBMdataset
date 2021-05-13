n = int(input())
cnts = [0]*n
alist = list(map(int,input().split()))
mod = 10**9+7

for i in range(n):
    cnts[alist[i]] += 1

p = n%2
if p == 1:
    cnts[0] += 1

for i in range(n):
    if p != (i%2):
        if cnts[i] != 2:
            print(0)
            exit()
    else:
        if cnts[i] != 0:
            print(0)
            exit()
print(pow(2,(n//2))%mod)