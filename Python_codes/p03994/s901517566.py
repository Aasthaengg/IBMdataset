s = input()
x = int(input())
tank = []
for c in list(s):
    if c=='a':
        tank.append(0)
    else:
        tank.append(ord('z') + 1 - ord(c))
res = ''
for i in range(len(tank)):
    if tank[i] == 0:
        res += s[i]
    elif tank[i] <= x:
        x -= tank[i]
        tank[i] = 0
        res += 'a'
    else:
        res += s[i]

c = res[-1]
x %= 26
if ord(c)+x <= ord('z'):
    res = res[:-1] + chr(ord(c)+x)
else:
    res = res[:-1] + chr(ord(c)+x-ord('z')+ord('a')-1)
print(res)