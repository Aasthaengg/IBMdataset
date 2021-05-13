S = input()
for i, s in enumerate(S, 1):
    if (i%2==1 and s=='L') or (i%2==0 and s=='R'):
        print('No')
        exit()
print('Yes')