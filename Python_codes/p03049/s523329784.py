import sys
N = int(sys.stdin.readline())
ss = []
for i in range(N):
    ss.append(sys.stdin.readline().rstrip())

incount = 0
has_ba = 0
has_b = 0
has_a = 0
for s in ss:
    incount += s.count('AB')
    if s[0] == 'B' and s[-1] == 'A':
        has_ba += 1
    elif s[0] == 'B':
        has_b += 1
    elif s[-1] == 'A':
        has_a += 1

res = incount
if has_a:
    res += has_ba
elif has_ba:
    has_a += 1
    has_ba -= 1
    res += has_ba
res += min(has_a, has_b)




# if has_ba:
#     res += has_ba - 1
#     has_ba = 1
# if has_b or has_a:
#     npair = min(has_b, has_a)
#     res += npair
#     has_b -= npair
#     has_a -= npair
# if has_ba and (has_b or has_a):
#     res += 1

print(res)
