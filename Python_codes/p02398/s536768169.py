x = input().split()

x_int = [int(i) for i in x]
y = [i for i in range(x_int[0],x_int[1]+1) if x_int[2]%i == 0]
print(len(y))