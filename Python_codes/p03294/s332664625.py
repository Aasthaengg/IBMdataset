import fractions
n = int(input())
lis = list(map(int,input().split()))
now = 1
for num in lis:
    now = (now * num)//fractions.gcd(now,num)
now -= 1
ans = sum([now%lis[i] for i in range(n)])
print(ans)
