import sys
n = list(str(input()))
for i in range(len(n)-2):
    if n[i] == n[i + 1] and n[i + 1] == n[i + 2]:
        print('Yes')
        sys.exit()
print('No')
