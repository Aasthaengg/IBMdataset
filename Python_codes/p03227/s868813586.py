ins = input().rstrip()
if len(ins) == 2:
    print(''.join(ins))
else:
    print(''.join(ins[::-1]))