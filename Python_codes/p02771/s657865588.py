char = list(map(str,input().split()))
if char.count(char[0]) == 2 or char.count(char[1]) == 2:
    print('Yes')
else:
    print('No')