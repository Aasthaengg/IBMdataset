n = int(input())
dic = {}
for i in range(1,n+1):
    s,p = map(str,input().split())
    dic.setdefault(s,[])
    dic[s].append([int(p),i])
#print(dic)
sort_list = sorted(dic)
for key in sort_list:
    sort_item = sorted(dic[key],reverse=True)
    #print(sort_item)
    for i in range(len(sort_item)):
        print(sort_item[i][1])
