N = input()

m = 0
for n in N:
    m += int(n)

if m % 9 == 0:
    print('Yes')
else:
    print('No')