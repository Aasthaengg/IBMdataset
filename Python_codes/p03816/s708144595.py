n=int(input())

t = list(map(int,input().split()))

memo = [0]*100000

for i in t:
    memo[i-1] += 1

sa = 0

for j in memo:
    if 1<j:
        sa += j-1

print(n-sa-sa%2)