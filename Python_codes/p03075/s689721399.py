a = [int(input()) for i in range(5)]
k = int(input())

for i in range(1, 5):
    if a[i] - a[0] > k:
        print(':(')
        exit()
print('Yay!')
