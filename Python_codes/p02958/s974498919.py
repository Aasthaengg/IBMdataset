n = int(input())
p = list(map(int, input().split()))
p2 = sorted(p)
diff = 0
for i in range(n):
    if p[i] != p2[i]:
        diff += 1
print("YES") if diff <=2 else print("NO")