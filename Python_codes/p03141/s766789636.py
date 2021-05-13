from sys import stdin
N = int(stdin.readline().rstrip())
data = []
for i in range(N):
    A,B = [int(x) for x in stdin.readline().rstrip().split()]
    data.append((A+B,A,B))
data.sort()
a = 0
b = 0
for ind,(i,j,k) in enumerate(data[::-1]):
    if ind % 2 == 0:
        a += j
    else:
        b += k
        
print(a-b)