n = int(input())
lis = list(map(int,input().split()))

lis.sort()

ans1 = lis[-1]

lis = lis[:-1]
half = ans1/2

ans2 = 0
length = 10**9+7

for i in lis:
    t = abs(half - i)
    if t < length:
        length = t
        ans2 = i
    

print(ans1, ans2)

