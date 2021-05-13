a, b = map(str, input().split())
if (int(a+b)**0.5).is_integer():
    print('Yes')
else:
    print('No')
