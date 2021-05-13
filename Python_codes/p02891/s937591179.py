# -*- coding: utf-8 -*-
s = input()
k = int(input())

if len(set(s)) == 1:
    print(len(s) * k // 2)
    exit()

count = []
tmp = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        tmp += 1
    if s[i] != s[i + 1]:
        count.append(tmp + 1)
        tmp = 0
count.append(tmp + 1)
#print(count)

flag = True
ans = 0
if s[0] == s[-1] and (count[-1] > 1 or count[0] > 1) and (count[-1] + count[0]) % 2 == 0:
    flag = False
if s[0] == s[-1]:
    if count[-1] == 1 and count[0] == 1:
        ans += k - 1
        flag = False
    else:
        ans += k - 1
        if count[-1] >= count[0]:
            count[-1] -= 1
        else:
            count[0] -= 1
#print(flag)
#print(ans)
#print(count)
for i in range(len(count)):
    if count[i] > 1:
        ans += (count[i] // 2) * k
if s[0] == s[-1] and count[-1] >= 1 and flag:
    #print("B")
    ans += 1
print(ans)
