n = int(input())
s = input()
e_l, e_sum = [], 0
w_l, w_sum = [], 0
for i in range(n):
    if s[i] == 'E':
        e_sum += 1
    else:
        w_sum += 1
    e_l.append(e_sum)
    w_l.append(w_sum)
for i in range(n):
    if i == 0:
        ans = e_l[n-1] - e_l[0]
    elif i == n:
        ans = max(ans, w_l[n-2])
    else:
        ans = min(ans, e_l[n-1] - e_l[i] + w_l[i-1])
print(ans)