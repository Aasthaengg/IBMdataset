N,T = map(int,input().split())

dic = {}
for i in range(N):
    c,t = map(int,input().split())
    dic[c] = t
list = []
for key, value in dic.items():
    if value <= T:
        list.append(key)

if len(list) > 0:
    print(min(list))
else:
    print('TLE')
