in_vars = input().split()

N = int(in_vars[0])
X = int(in_vars[1])
T = int(in_vars[2])

if N % X == 0:
    time = (N // X )*T
else:
    time = (N // X + 1)*T

print(time)