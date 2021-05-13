num = input().split()
num_i = [int(s) for s in num]

a,b,c = num_i
min_1 = a+b
min_2 = b+c
min_3 = c+a

min_a1 = min(min_1, min_2)
min_a = min(min_a1, min_3)
print(min_a)