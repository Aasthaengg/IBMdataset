a, b, c = map(int, input().split())
flag = False
if c-a-b > 0:
    if (c-a-b)**2-4*a*b > 0:
        flag = True
print('Yes' if flag else 'No')
