K = int(input())
a = 7 % K
mods = []

i = 0
found = False
while (i <= K):
    i += 1
    if a == 0:
        print(i)
        found = True
        break
    a = (10 * a + 7) % K

if not found:
    print(-1)