N = input()
if len(set(N[0:3]))==1 or len(set(N[1:4]))==1:
    print('Yes')
else:
    print('No')