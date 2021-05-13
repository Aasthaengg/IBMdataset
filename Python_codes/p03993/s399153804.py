N = int(input())
an = list(map(int, input().split()))
ans = 0
for i, a in enumerate(an):
    if an[a-1] == i+1:
        ans += 1
print(ans//2)