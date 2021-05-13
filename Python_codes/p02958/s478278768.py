n = int(input())
p = list(map(int, input().split()))
x = 0
for i in range(n):
    if i + 1 != p[i]:
        x += 1
print("YES" if  x == 0 or x == 2 else "NO")