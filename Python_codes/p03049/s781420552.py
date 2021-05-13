n = int(input())

ans = 0
last_a = 0
first_b = 0
cnt = 0

for i in range(n):
    s = input()
    ans += s.count("AB")
    if s[-1] == "A":
        last_a += 1
    if s[0] == "B":
        first_b += 1
    if s[-1] == "A" and s[0] == "B":
        cnt += 1

if last_a == first_b & cnt > 0:
    ans += min(last_a, first_b) - 1
else:
    ans += min(last_a, first_b)

print(ans)