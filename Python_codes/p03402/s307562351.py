a, b = [int(i) for i in input().split(" ")]
h = 96
w = 96
ca = 512 - a
cb = 512 - b

print(w, h)

m = [[False for j in range(0, h)] for i in range(0, w)]

for i in range(0, 32 * 3):
    for j in range(0, 32 * 3):
        m[i][j] =  (i // 3 + j // 3) % 2 == 1

for i in range(0, min(ca, 15)):
    for j in range(i * 6 + 3, i * 6 + 6):
        m[0][j] = False
        
ca -= min(ca, 15)

for i in range(0, min(ca, 15)):
    for j in range(i * 6 + 3, i * 6 + 6):
        m[j][0] = False
    
ca -= min(ca, 15)

k = 0
while ca > 0:
    for i in range(0, min(ca, 16)):
        m[3 * k + 2][6 * i + 3] = False
    ca -= min(ca, 16)
    k += 1
    for i in range(0, min(ca, 15)):
        m[3 * k + 2][6 * i + 6] = False
    ca -= min(ca, 15)
    k += 1
    
    
for i in range(0, min(cb, 15)):
    for j in range(i * 6 + 3, i * 6 + 6):
        m[95][j] = True
        
cb -= min(cb, 15)

if cb > 0:
    cb -= 1
    m[93][95] = True
    m[94][95] = True
    m[95][95] = True
    m[95][94] = True
    m[95][93] = True

for i in range(0, min(cb, 15)):
    for j in range(i * 6 + 3, i * 6 + 6):
        m[92 - j][95] = True
    
cb -= min(cb, 15)

k = 0
while cb > 0:
    for i in range(0, min(cb, 15)):
        m[92 - 3 * k][6 * i + 6] = True
    cb -= min(cb, 15)
    k += 1
    for i in range(0, min(cb, 16)):
        m[92 - 3 * k][6 * i + 3] = True
    cb -= min(cb, 16)
    k += 1

for i in range(0, 32 * 3):
    s = ""
    for j in range(0, 32 * 3):
        if m[i][j]:
            s = s + "#"
        else:
            s = s + "."
    print(s)