print('Yes' if (lambda l: l[0] + l[1] - l[2])(list(map(int, input().split()))) >= 0 else 'No')
