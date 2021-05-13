s = int(input())

v = [False] * 1000001
v[s] = True

i = 1
while True:
    i += 1
    if s % 2 == 0:
        s = s // 2
    else:
        s = 3 * s + 1
    
    if v[s]:
        break
    else:
        v[s] = True

print(i)