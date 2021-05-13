x = str(input())
y = str(input())

s = []
for i in x:
    s.append(i)
p = []
for i in y:
    p.append(i)

n = len(p)
flag = 0
for i in range(len(s)):
    if i+n > len(s):
        if s[i:]+s[0:(i+n)%len(s)] == p:
            print('Yes')
            flag = 1
            break
    else:
        if s[i:i+n] == p:
            print('Yes')
            flag = 1
            break

if flag == 0:
    print('No')