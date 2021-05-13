n = int(input()); a = list(map(int, input().split())); b = 0
for i in range(n):
    if a[i]%2 == 1: b += 1
print("YES") if b%2 == 0 else print("NO")