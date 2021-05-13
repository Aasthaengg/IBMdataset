N = int(input())
V = list(map(int,input().split()))

V.sort()
sum = 0
for i,v in enumerate(V):
    if i == 0:
        sum += v
    sum = float((sum + v) / 2)

print(sum)