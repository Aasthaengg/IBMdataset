N = int(input())
s = input()
tmp = 0
for i in range(N):
    if (s[i] == "R"):
        tmp += 1
    else:
        tmp -= 1

if (tmp > 0):
    print("Yes")
else:
    print("No")