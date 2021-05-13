S = set(input())
a = set([chr(i) for i in range(ord('a'), ord('z')+1)])
result = sorted(list(a-S))
if len(result) == 0:
    print('None')
else:
    print(result[0])