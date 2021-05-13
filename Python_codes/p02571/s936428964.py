s = input()
t = input()

diff = 0
min_diff = len(t)

for cnt_s in range(0, len(s) - len(t)+1):
    diff = 0
    for cnt_t in range(0, len(t)):
        if s[cnt_s + cnt_t] != t[cnt_t]:
            diff += 1
    if min_diff > diff:
        min_diff = diff

print(min_diff)
