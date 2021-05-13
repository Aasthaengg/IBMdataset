n = [int(input()) for n in range(5)]
k = int(input())

if n[4] - n[0] <= k and n[3] - n[0] <= k and n[2] - n[0] <= k and n[1] - n[0] <= k:
    print('Yay!')
else:
    print(':(')
