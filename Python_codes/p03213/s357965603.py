from collections import defaultdict
N=int(input())
fac = defaultdict(int)

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
            fac[i] += cnt

    if temp!=1:
        arr.append([temp, 1])
        fac[temp] += 1 

    if arr==[]:
        arr.append([n, 1])
        fac[n] += 1
    return arr

for num in range(2, N+1):
    factorization(num)

ans = 0

num_74 = set()
num_24 = set()
num_14 = set()
num_4 = set()
num_2 = set()
for key, value in fac.items():
    if value >= 74:
        num_74.add(key)
    if value >= 24:
        num_24.add(key)
    if value >= 14:
        num_14.add(key)
    if value >= 4:
        num_4.add(key)
    if value >= 2:
        num_2.add(key)
#1
ans += len(num_74)

#2
ans += len(num_24) * (len(num_2)-1)
# ans += len(num_2.difference(num_24)) * (len(num_24))*(len(num_24)-1)//2 + len(num_24) * (len(num_24)-1)*(len(num_24)-2)//2


#3
ans += len(num_14) * (len(num_4) - 1)
# ans += len(num_4.difference(num_14)) * (len(num_14))*(len(num_14)-1)//2 + len(num_14) * (len(num_14)-1) * (len(num_14) - 2) //2

#4
ans += len(num_2.difference(num_4)) * len(num_4)*(len(num_4)-1)//2 + len(num_4) * (len(num_4)-1)*(len(num_4)-2)//2


print(ans)

