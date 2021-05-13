N = map(int, input().split())
A = [int(i) for i in input().split()]
oddCount = 0
for a in A:
    if a % 2:
        oddCount += 1
print("YES" if oddCount % 2 == 0 else "NO")
