l = [int(input()) for _ in range(5)]
k = int(input())
if l[4] - l[0] > k:
    print(':(')
else:
    print('Yay!')