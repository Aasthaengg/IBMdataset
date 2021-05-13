N = int(input())

c = 4
d = 7
result = False

for i in range(26):
    for j in range(15):
        if (N == c * i + d * j):
            result = True
            break

if result == True:
    print('Yes')
else:
    print('No')
