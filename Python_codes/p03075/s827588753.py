x = []
for i in range(5):
    i = int(input())
    x.append(i)
k = int(input())

if (x[4] - x[0]) > k:
    print(':(')
else:
    print('Yay!')