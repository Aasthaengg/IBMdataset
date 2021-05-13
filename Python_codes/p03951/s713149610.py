N = int(input())
s = input()
t = input()

find = False
for i in range(N):
    mae = s[i:]
    ushiro = t[0:N-i]
    if mae == ushiro:
        find = True
        break
if find:
    print(N+i)
else:
    print(N*2)
