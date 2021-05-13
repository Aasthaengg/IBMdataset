# AGC 026: A – Colorful Slimes 2
N = int(input())
a = [int(s) for s in input().split()]

for i in range(N - 1):
    if a[i + 1] == a[i]:
        a[i + 1] = 0

print(a.count(0))