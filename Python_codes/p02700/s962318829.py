A, B, C, D = [int(i) for i in input().split(' ')]
print('Yes' if int((A - 1) / D) >= int((C - 1) / B) else 'No')
