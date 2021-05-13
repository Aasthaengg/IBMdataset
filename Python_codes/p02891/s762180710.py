s = list(input())
k = int(input())

l = len(s)

ss = s + s
ll = len(ss)

single = 0
cnt = 0

for i in range(1, l):
    if s[i - 1] == s[i]:
        if cnt == 0:
            single += 1
            cnt = 1
        else:
            if cnt % 2 == 0:
                single += 1
                cnt += 1
            else:
                cnt += 1
    else:
        cnt = 0

double = 0
cnt = 0

for i in range(1, ll):
    if ss[i - 1] == ss[i]:
        if cnt == 0:
            double += 1
            cnt = 1
        else:
            if cnt % 2 == 0:
                double += 1
                cnt += 1
            else:
                cnt += 1
    else:
        cnt = 0

if len(set(s)) == 1:
    ans = double * (k // 2) + single * (k % 2)
elif single * 2 == double:
    ans = single * k
else:
    ans = single + (single + 1) * (k - 1)

# print(single, double)
print(ans)
