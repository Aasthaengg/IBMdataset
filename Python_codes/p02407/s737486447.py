n = int(input())
x = input().split()
x_int = [int(i) for i in x]
y = list(range(n))

for i in range(n):
     y[-i-1] = x_int[i]
y_str = [str(i) for i in y]
print(' '.join(y_str))