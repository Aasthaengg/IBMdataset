num = input().split()
num_i = [int(s) for s in num]

a, b, c = num_i

if (c >= a and b >= c):
    print('Yes')
else:
    print('No')