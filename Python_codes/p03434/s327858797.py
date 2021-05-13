# 088 B
N = int(input())
a = list(map(int, input().split()))
A = 0
B = 0
aa = sorted(a)
for i in range(0, N, 2):
    A += aa[-i-1]
    if (i+2)<=N:
        B += aa[-i-2]
print(A-B)
