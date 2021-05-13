s = input()

n = len(s)

if n %2 != 0:
    print('No')
elif s == 'hi'*(n//2):
    print('Yes')
else:
    print('No')