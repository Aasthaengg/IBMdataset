from collections import defaultdict

N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

dic = defaultdict(int)
for d in D:
    dic[d] += 1

for t in T:
    if dic[t]:
        dic[t] -= 1
    else:
        print ('NO')
        exit()

print ('YES')