s = input()
import sys
n = len(s)
kisuu = ["R","U","D"]
guusuu = ["L","U","D"]

for i in range(n):
    if i%2 == 0:
        if s[i] not in kisuu:
            break
    else:
        if s[i] not in guusuu:
            break
else:
    print("Yes")
    sys.exit()
print("No")