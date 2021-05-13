num = input().split()
num_i = [int(s) for s in num]
a, b, c, d = num_i

if((abs(a-b) <= d) and (abs(c-b)) <= d):
    print('Yes')
elif((abs(a-c)) <= d):
    print('Yes')
else:
    print('No')