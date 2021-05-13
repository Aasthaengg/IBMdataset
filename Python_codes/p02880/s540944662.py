N = int(input())
for i in range(1,10):
    if not N%i == 0:
        continue
    rest = N/i
    if rest<10:
        print('Yes')
        exit()

print('No')