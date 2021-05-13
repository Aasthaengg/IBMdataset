s = list(input())
t = list(input())

s.sort()
t.sort(reverse=True)
alp = [chr(i) for i in range(97, 97+26)]

n = min(len(s), len(t))
flag = True
for i in range(n):
    if alp.index(s[i]) < alp.index(t[i]):
        print('Yes')
        flag = False
        break
    elif alp.index(s[i]) > alp.index(t[i]):
        print('No')
        flag = False
        break
    else:
        continue

if flag:
    if len(s) < len(t):
        print('Yes')
    else:
        print('No')