s = input()
ans = True if len(s)%2 == 0 else False
for i in range(len(s)//2):
    if i%2 == 1:
        continue
    if s[i:i+2] != "hi":
        ans = False

print("Yes" if ans else "No")