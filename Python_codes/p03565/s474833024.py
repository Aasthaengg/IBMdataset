s_ = list(str(input()))
t = list(str(input()))

n = len(s_)
m = len(t)

if m > n:
    print('UNRESTORABLE')
    exit()

import copy
ans = []
for i in range(n-m+1):
    if s_[i] == t[0] or s_[i] == '?':
        temp = copy.copy(s_)
        for j in range(i, i+m):
            #print(i, temp)
            if s_[j] == '?':
                temp[j] = t[j-i]
            elif s_[j] == t[j-i]:
                continue
            else:
                break
        else:
            for k in range(n):
                if temp[k] == '?':
                    temp[k] = 'a'
            ans.append(''.join(temp))
if ans:
    ans.sort()
    print(ans[0])
else:
    print('UNRESTORABLE')
