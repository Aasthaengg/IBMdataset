x = input().split()
a, b, c = int(x[0]), int(x[1]), int(x[2])
div_list = [i for i in range(a, b + 1) if c % i == 0]
print(len(div_list))
