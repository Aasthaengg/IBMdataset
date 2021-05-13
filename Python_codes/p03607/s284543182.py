N = int(input())
dic_a = {}
for i in range(N):
    a= int(input())
    if a in dic_a:
        dic_a[a] +=1
        dic_a[a] = dic_a[a]%2
    else:
        dic_a[a] = 1
print(sum(list(dic_a.values())))
