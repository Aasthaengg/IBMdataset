N, M = map(int, input().split(' '))
x = 2 ** M
y = N-M
print((1900*M+100*y)*x)