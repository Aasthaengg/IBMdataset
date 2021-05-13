from collections import defaultdict

n = int(input())
dic = defaultdict(int)

for i in range(1,n+1):
    s = str(i)
    dic[int(s[0]),int(s[-1])] += 1

point = 0

for i in range(1,10):
    for j in range(1,10):
        point += dic[i,j]*dic[j,i]

print(point)