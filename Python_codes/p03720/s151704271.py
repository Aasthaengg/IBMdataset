n,m=[int(i) for i in input().split()]

#都市nがキー
keys=[i for i in range(1,n+1)]
#print(keys)
values=[0]*n
#print(values)
a_dic=dict(zip(keys,values))
#print(a_dic)

for i in range(m):
    a,b=[int(i) for i in input().split()]
    #print(a,b)
    a_dic[a]+=1
    a_dic[b]+=1


#print(a_dic)

#都市n個のvalueを出力していく    
for i in range(1,n+1):
    print(a_dic[i])

   