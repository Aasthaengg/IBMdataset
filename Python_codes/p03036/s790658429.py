from sys import stdin

r, d, x = (int(x) for x in stdin.readline().rstrip().split())

for i in range(1, 11):
    print(r*x - d)
    x = r*x - d