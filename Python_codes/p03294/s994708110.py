N = int(input())
A = list(map(int, input().split()))
f_max = 0
for a in A:
    f_max += a-1
print(f_max)