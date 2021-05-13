n, k = list(map(int, input().split()))
exp = list(map(lambda x: (1+int(x))/2, input().split()))

c = sum(exp[:k])
cmax = c

for i in range(n-k):
    c -= exp[i]
    c += exp[i+k]

    if c > cmax:
        cmax = c

print(cmax)