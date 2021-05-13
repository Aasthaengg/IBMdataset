a,b = map(int,input().split())

c=[int(input()) for i in range(a)]

minbox = min(c)
flag = 0

for i in c:
    b = b - i
    flag += 1


while True:
    if b < minbox:
        break
    else:
        b = b - minbox
        flag += 1
        continue
    break
print(flag)