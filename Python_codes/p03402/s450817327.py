a,b = map(int,input().split())

space = [0 for i in range(100*100)]
#半分で塗り分け 白0、黒1
for i in range(len(space)):
    if i >= 5000:
        space[i] = 1

while(True):
    for i in range(0,5000,6):
        if a > 1:
            space[i] = 1
            a -= 1
        else:
            break

    for j in range(5000,10000,6)[::-1]:
        if b > 1:
            space[j] = 0
            b -= 1
        else:
            break

    if a == 1 and b == 1:
        break

ans = ""

for (i,cell) in enumerate(space):
    if i % (100*(i//100)+99) == 0 and i != 0:
        if cell == 0:
            ans = ans + "#\n"
        else:
            ans = ans + ".\n"
    else:
        if cell == 0:
            ans = ans + "#"
        else:
            ans = ans + "."
print(100,100)
print(ans)
