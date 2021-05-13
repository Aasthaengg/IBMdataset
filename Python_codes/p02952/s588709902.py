n=input()
s = int(n)

if len(n) <= 1:
    print(n)
if 2 <= len(n) <3:
    print(9)
if 3<= len(n) <4:
    print(s-99 + 9)
if 4 <= len(n) < 5:
    print(999-99+9)
if 5 <= len(n) < 6:
    print(s -9999 + 999 - 99 + 9)
if len(n) == 6:
    print(99999-9999 + 999 -99 +9)