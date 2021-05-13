n = int(input())
t, a = map(int, input().split())
listh = list(map(int, input().split()))
temp = 100000
index = 0

for i in range(n):
    diff = abs((t - listh[i] * 0.006)-a)
    if temp > diff:
        temp = diff
        index = i+1

print(index)
