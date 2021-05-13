a = list(map(int,input().split()))
dic = {}
for i in range(len(a)):
    dic.setdefault(a[i],0)
    dic[a[i]]+=1
print(len(dic))