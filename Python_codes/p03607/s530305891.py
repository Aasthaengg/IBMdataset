dic = {}
N = int(input())

for i in range(N):
    a = int(input())

    if a in dic:
        dic.pop(a)
    else:
        dic[a]=1

print(len(dic))