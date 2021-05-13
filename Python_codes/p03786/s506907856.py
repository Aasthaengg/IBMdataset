n = int(input())
A = map(int, input().split())

s = sorted(A)

ac = 0
startI = 0
for i, a in enumerate(s):
    if i == len(s) - 1:
        print(len(s) - startI)
        exit()

    ac += a

    if ac * 2 < s[i+1]:
        startI = i+1





