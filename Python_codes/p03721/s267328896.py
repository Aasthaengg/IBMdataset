N,K = [int(i) for i in input().split()]
dic = {}
sum = 0

for i in range(N):
    a,b = [int(i) for i in input().split()]
    if a in dic:
        dic[a] += b
    else:
        dic[a] = b

dic = sorted(dic.items())

for i in range(len(dic)):
    sum += dic[i][1]
    if K <= sum:
        print(dic[i][0])
        break
