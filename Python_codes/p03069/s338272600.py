n = int(input())
s = input()
migi = s.count(".")
hidari = 0
ans = migi
for i in range(n):
    if s[i] == "#":
        hidari += 1
    elif s[i] == ".":
        migi -= 1
    ans = min(ans,hidari+migi)
print(ans)