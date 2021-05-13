N = int(input())
D = list(map(int, input().split()))
dic = {}
ABCs = 0
count = 0

for i in range(N):
    if D[i] in dic:
        dic[D[i]] += 1
    else:
        dic[D[i]] = 1

diffs = sorted(dic.keys())

for i in range(diffs[-1]+1):
    if i in dic:
        ABCs += dic[i]
    if ABCs == N / 2:
        count += 1

print(count)
