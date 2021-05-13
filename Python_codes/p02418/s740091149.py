text = input().strip('\n') * 2
pattern = input().strip('\n')
if len(pattern) <= len(text) / 2 and pattern in text:
    print('Yes')
else:
    print('No')
