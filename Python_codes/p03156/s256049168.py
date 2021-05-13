#%%
n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))

x1 = 0
x2 = 0
x3 = 0

for i in range(n):
    if p[i] <= a:
        x1 += 1
    elif a < p[i] <= b:
        x2 += 1
    else:
        x3 += 1

print(min(x1, x2, x3))