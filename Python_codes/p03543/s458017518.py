n = input()

if len(set(n)) == 1:
    print('Yes')
    exit()

if ((n[0] == n[1]) & (n[1] == n[2])) ^ ((n[1] == n[2]) & (n[2] == n[3])):
    print('Yes')
    exit()
print('No')
