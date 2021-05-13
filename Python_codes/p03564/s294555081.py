N = int(input())
K = int(input())
a = 1

for i in range(N):
    if a*2 > a+K:
        a += K
    else:
        a *= 2

print(a)