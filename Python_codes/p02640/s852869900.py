import sys

X, Y = map(int,input().split())

# i = カメの数
for i in range(X + 1):
    if i * 2 + (X - i) * 4 == Y:
        print('Yes')
        sys.exit()
print('No')