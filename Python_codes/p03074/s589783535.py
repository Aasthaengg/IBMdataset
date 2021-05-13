from itertools import accumulate
n, k = map(int, input().split())
s = [i for i in input()]
zero_one = [0]
if s[0] == "0":
    zero_one.append(0)
s_ = s[0]
cnt = 0
for i in range(n):
    if s_ == s[i]:
        cnt += 1
    else:
        zero_one.append(cnt)
        cnt = 1
        s_ = s[i]
zero_one.append(cnt)
if s[-1] == "0":
    zero_one.append(0)
ans = 0
l = len(zero_one)
zero_one = list(accumulate(zero_one))
for i in range(0, l, 2):
    ans = max(ans, zero_one[min(l-1, i+2*k+1)] - zero_one[i])
print(ans)