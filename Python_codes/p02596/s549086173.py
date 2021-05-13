k = int(input())

if k == 1:
    print('1')
    exit()
if k % 2 == 0 or k % 5 == 0:
    print('-1')
    exit()

k *= 9
a = 10
for i in range(10*k):
    if (7 * (a - 1 + k)) % k == 0:
        print(str(i+1))
        exit()
    a = (a*10) % k
