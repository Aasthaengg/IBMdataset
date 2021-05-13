p = input().split()

k = int(p[0])
s = int(p[1])

x = -1
y = -1
z = 0
answer = 0

for num in range(k+1):
    x += 1
    y = -1
    for n in range(k+1):
        y += 1
        z = s - x - y
        if 0 <= z and z <= k:
            answer += 1
 



print(answer)     