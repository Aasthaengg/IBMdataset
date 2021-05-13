from sys import exit, stdin
X, Y = [int(_) for _ in stdin.readline().rstrip().split()]
for i in range(1, 11):
    if X*i % Y != 0:
        print(X*i)
        exit()
print(-1)