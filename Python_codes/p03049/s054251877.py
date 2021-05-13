n = int(input())
ans = 0
cnt_a, cnt_b, cnt_ab  = 0, 0, 0
for i in range(n):
    s = input()
    ans += s.count("AB")
    if s[-1] == "A":
        cnt_a += 1
    if s[0] == "B":
        cnt_b += 1
    if s[0] == "B" and s[-1] == "A":
        cnt_ab += 1
#print(cnt_a, cnt_b, cnt_ab)
print(ans + min(cnt_a, cnt_b) if cnt_ab < max(cnt_a, cnt_b) or cnt_b == 0 else ans + (cnt_ab - 1))