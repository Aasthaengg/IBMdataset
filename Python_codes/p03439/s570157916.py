n = int(input())
print(0)
L = R = input()
if L == "Vacant":
    exit()

l = 0
r = n
while True:
    m = (l + r) // 2
    print(m)
    M = input()
    if M == "Vacant":
        exit()
    if (M == L) ^ ((m - l) % 2 == 1):
        l = m
        L = M
    else:
        r = m
        R = M

