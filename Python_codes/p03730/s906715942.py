import sys
a, b, c = map(int, input().split())

res = a%b

for i in range(1, b):
    if (res*i)%b == c:
        print('YES')
        sys.exit()
        break
print('NO')