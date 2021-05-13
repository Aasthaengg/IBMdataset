n,t = map(int, input().split())

dic = {}
for i in range(n):
    a,b = map(int, input().split())
    dic[a] = b

dic = sorted(dic.items(), key = lambda x : x[0])

for i,j in dic:
    if j <= t:
        print(i)
        exit()
print('TLE')