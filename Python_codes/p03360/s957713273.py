abc = list(map(int, input().split()))
k = int(input())
mx = max(abc)
x2 = mx
for i in range(k):
    x2 *= 2
print(x2 + sum(abc) - mx)
