s = input()
s = s * 2
p = input()

for offset in range(len(s) - len(p) + 1):
    if s[offset:offset+len(p)] == p[:]:
        print("Yes")
        break
else:
    print("No")