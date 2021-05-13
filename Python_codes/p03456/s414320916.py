a, b = map(str, input().split())
s = a + b
s = int(s)
ans = 0

for i in range(s):
    if i**2 == s:
        print ("Yes")
        exit()
print ("No")