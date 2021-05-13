n = int(input())

a_end = 0
b_start = 0
a_b = 0
cnt = 0

for _ in range(n):
    s = input()
    cnt += s.count("AB")
    if s[0] == "B" and s[-1] == "A":
        a_b += 1
        continue
    if s[0] == "B":
        b_start += 1
    if s[-1] == "A":
        a_end += 1

if a_end == 0 and b_start == 0:
    tmp = max(a_b - 1, 0)
else:
    tmp = min(a_end,  b_start) + a_b
print(cnt + tmp)