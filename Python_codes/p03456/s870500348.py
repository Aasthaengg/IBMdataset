import sys
a, b = input().split()
st = a + b
val = int(st)

for i  in range(val):
    if i * i == val:
        print('Yes')
        sys.exit()
print('No')