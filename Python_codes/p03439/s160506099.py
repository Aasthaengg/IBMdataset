n = int(input())
print(0)
s = input()
if s == "Vacant":
    exit()
a = s
l = 0
r = n
while True:
    m = (l + r) // 2
    print(m)
    s = input()
    if s == "Vacant":
        exit()
    if (s == a) ^ ((m - l) % 2 == 1):
        l = m
        a = s
    else:
        r = m