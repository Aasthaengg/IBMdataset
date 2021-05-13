from sys import stdin

n = int(stdin.readline().rstrip())
B = [int(x) for x in stdin.readline().rstrip().split()]

B.append(1e+5 + 3)

sum = B[0]

for i in range(1, n):
    sum += min(B[i-1: i+1])

print(sum)