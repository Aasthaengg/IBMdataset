a,b,c=map(int,input().split())
dic={}
dic[a]=1
dic[b]=1
dic[c]=1
dic[a]+=1
dic[b]+=1
dic[c]+=1
print(list(dic.keys())[list(dic.values()).index(2)])
