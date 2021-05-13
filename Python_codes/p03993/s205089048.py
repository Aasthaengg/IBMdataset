n = int(input())
la = [int(w)-1 for w in input().split()]

ans = 0
for i in range(n):
    if la[la[i]] == i:
        ans += 1
print(ans//2)
