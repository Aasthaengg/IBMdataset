N = int(input())
c = 1
for i in range(1,10):
    if N%i == 0:
        s = N//i
        if 1 <= s <= 9:
            print('Yes')
            c = 0
            break

if c:
    print('No')