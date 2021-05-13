import sys
N = int(sys.stdin.readline().rstrip())

ans = 0
cnt_start_b = 0
cnt_end_a = 0
cnt_start_b_end_a = 0

for _ in range(N):
    s = sys.stdin.readline().rstrip()
    ans += s.count("AB")
    if s[0] == "B" and s[-1] == "A":
        cnt_start_b_end_a += 1
    elif s[0] == "B":
        cnt_start_b += 1
    elif s[-1] == "A":
        cnt_end_a += 1

if cnt_start_b_end_a > 0:
    if cnt_end_a == cnt_start_b == 0:
        ans += cnt_start_b_end_a - 1
    elif cnt_end_a == 0:
        ans += cnt_start_b_end_a
    elif cnt_start_b == 0:
        ans += cnt_start_b_end_a
    else:
        ans += cnt_start_b_end_a + 1 + min(cnt_end_a - 1, cnt_start_b - 1)
else:
    ans += min(cnt_end_a, cnt_start_b)
print(ans)