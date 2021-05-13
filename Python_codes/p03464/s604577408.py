from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
low, high = 2, 2

for a in A[::-1]:
    low += (-low) % a
    high -= high % a
    high += (a-1)

if low > high:
    print(-1)
else:
    print(low, high)