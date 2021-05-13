def check(s, p):
    if s == p:
        return 1
    else:
        return 0

s = input()
p = input()

n = 0
answer = 0
while n < len(s) and answer == 0:
    answer = check(s[:len(p)], p)
    s0 = s[0:1]
    s1 = s[1:]
    s = s1 + s0
    n += 1

if answer:
    print("Yes")
else:
    print("No")