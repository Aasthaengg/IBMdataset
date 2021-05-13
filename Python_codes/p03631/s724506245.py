N = input()
if N[::1] == N[::-1]:
    print('Yes')
else:
    print('No')