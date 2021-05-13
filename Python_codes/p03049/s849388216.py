N = int(input())

ans = 0
top_b = 0
last_a = 0
top_b_and_last_a = 0

for _ in range(N):
    s = input()
    ans += s.count("AB")
    if s[0] == "B" and s[-1] == "A":
        top_b_and_last_a += 1
    elif s[0] == "B":
        top_b += 1
    elif s[-1] == "A":
        last_a += 1

ans += max(0, top_b_and_last_a - 1)
if top_b_and_last_a and top_b:
    top_b -= 1
    ans += 1
if top_b_and_last_a and last_a:
    last_a -= 1
    ans += 1
ans += min(top_b, last_a)

print(ans)