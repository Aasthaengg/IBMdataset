a, b = list(map(int, input().split()))

c = 0

for i in range(a, b+1):
    s = str(i)
    f = True
    for j in range(len(s)):
        #print(s[j], s[-j], i)
        if s[j] != s[-j-1]:
            f = False
            break
    if f:
        #print(i)
        c += 1

print(c)