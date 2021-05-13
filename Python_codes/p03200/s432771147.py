s = list(input())
n = len(s)
ans = 0
count = 0

for i in range(n):
    if s[i] == "W":
        ans += i
        count += 1

print(ans-count*(count-1)//2)