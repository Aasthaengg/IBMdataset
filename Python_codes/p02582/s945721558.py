s = input("")
Scnt = 0
Smem = 0

for i in range(len(s)):
    if s[i] == "S":
        Scnt += 1
        Smem = i

if Scnt == 3:
    print(0)
elif Scnt == 2:
    print(1)
elif Scnt == 0:
    print(3)
elif Scnt == 1 and Smem == 1:
    print(1)
elif Scnt == 1 and Smem != 1:
    print(2)