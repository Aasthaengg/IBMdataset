s = input()
n = len(s)
# RLに集まる、RRLLで偶数なら等分される、RLLで奇数なら少ない方に＋1
right = []
left = []
cnt = 0
for i in range(n):
    if s[i] == "R":
        cnt += 1
    else:
        cnt = 0
    right.append(cnt)
cnt = 0
for i in reversed(range(n)):
    if s[i] == "L":
        cnt += 1
    else:
        cnt = 0
    left.append(cnt)
left = left[::-1]
ans = []
for i in range(n-1):
    if len(ans)-1 == i:
        continue
    if s[i] == 'R' and s[i+1] == "L":
        total = right[i] + left[i+1]
        if total % 2 == 0:
            ans.append(total//2)
            ans.append(total//2)
        else:
            if left[i+1] % 2 == 0:
                ans.append(total//2+1)
                ans.append(total//2)
            else:
                ans.append(total//2)
                ans.append(total//2+1)
    else:
        ans.append(0)
if len(ans) != n:
    ans.append(0)
if s[0] == "L":
    ans[0] = left[0]
if s[-1] == "R":
    ans[-1] = right[-1]
print(*ans)
