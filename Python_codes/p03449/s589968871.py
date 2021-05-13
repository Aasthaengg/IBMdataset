import sys

N = int(sys.stdin.readline())
data = sys.stdin.readlines()

for i in range(2):
    data[i] = data[i].split(' ')
    data[i] = [int(j.replace('\n', '')) for j in data[i]]

set = [0]*N
for i in range(N):
    candy = 0
    candy = sum(data[0][0:i+1]) + sum(data[1][i:N])
    set[i] = candy

print(max(set))



