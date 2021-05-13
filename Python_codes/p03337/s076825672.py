num = input().split()
num_i = [int(s) for s in num]
a, b = num_i

print(max(a+b, a-b, a*b))