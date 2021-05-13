from sys import stdin


n,k = [int(x) for x in stdin.readline().rstrip().split()]

if n%k == 0:
    print(0)
    exit()
else:
    print(1)