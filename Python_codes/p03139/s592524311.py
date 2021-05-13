N, A, B = [int(i) for i in input().split()]

max = min([A, B])


num = A + B - N
if (num <= 0):
    minor = 0

else:
    minor = num

print(max, minor)