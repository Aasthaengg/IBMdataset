inputs = [int(s) for s in input().split()]
n = inputs[0]
k = inputs[1]

rest = n - k

if(k == 1):
    print(0)
else:
    print(rest)

