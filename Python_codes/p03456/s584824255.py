a, b = map(str, input().split())
s = int(a+b)
for i in range(1, s+1):
    if i**2 == s:
        print('Yes')
        exit()
else:
    print('No')
