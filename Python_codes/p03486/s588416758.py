p = input()
q = input()

s = list(p)
t = list(q)

s.sort()
t.sort()
answer = True

for i in range(len(s)):
    front = s[i]
    rear = t.pop()
    f = ord(front)
    r = ord(rear)
    if t == []:
        answer = False
        break
    if f == r:
        continue
    elif f < r:
        answer = True
        break
    else:
        answer = False
        break

if answer:
    print('Yes')
else:
    print('No')
