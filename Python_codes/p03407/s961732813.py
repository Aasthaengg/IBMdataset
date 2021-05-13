num = input().split()
num_i = [int(s) for s in num]
a, b, c = num_i

if(a+b>=c):
    print('Yes')
else:
    print('No')