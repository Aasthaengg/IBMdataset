num = input().split()
num_i = [int(s) for s in num]

X, t = num_i

if (X-t)>0:
    print(X-t)
else:
    print('0')