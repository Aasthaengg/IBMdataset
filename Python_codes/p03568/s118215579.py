N = int(input())
A = list(map(int, input().split()))
t = 1
for a in A:
    if a & 1 == 0:
        t *= 2
print(pow(3, N)-t)