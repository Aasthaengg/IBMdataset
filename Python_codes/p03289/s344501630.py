s = input()
n = len(s)
ans = 1
if s[0] != "A":
    ans *= 0
if not (97 <= ord(s[1]) <= 122):
    ans *= 0
if not (97 <= ord(s[-1]) <= 122):
    ans *= 0

check = 0
for i in range(1, n - 1):
    if s[i] == "C":
        check += 1
print(["WA", "AC"][ans & (check == 1)])
