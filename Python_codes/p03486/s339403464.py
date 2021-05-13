if ''.join(sorted(input())) < ''.join(sorted(input(), reverse=True)):
    print('Yes')
else:
    print('No')
