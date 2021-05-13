N = int(input())
D = list(map(int, input().split()))
dic = {}
ABCs = 0
count = 0
flag = 0

for i in range(N):
    if D[i] in dic:
        dic[D[i]] += 1
    else:
        dic[D[i]] = 1

diffs = sorted(dic.keys())

for k in range(diffs[-1]+1):
    if flag == 0:
        if ABCs == N / 2:
            count += 1
            flag += 1
    else:
        if ABCs > N / 2:
            break
        count += 1

    if k in dic:
        ABCs += dic[k]

print(count)
