n = int(input())
l = list(map(int,input().split()))

l_dic = {}
for i in range(n):
    if l[i] not in l_dic:
        l_dic[l[i]] = 0
    l_dic[l[i]] += 1

l_item = list(l_dic.items())
l_item.sort(key = lambda x:x[0])

if len(l_dic) < 3:
    print(0)
    exit()

ans = 0
for i in range(len(l_item)):
    for j in range(i+1,len(l_item)):
        for k in range(j+1,len(l_item)):
            if l_item[i][0] + l_item[j][0] > l_item[k][0] and l_item[i][0] + l_item[k][0] > l_item[j][0] and l_item[k][0] + l_item[j][0] > l_item[i][0]:
                ans += 1*l_item[i][1]*l_item[j][1]*l_item[k][1]

print(ans)




