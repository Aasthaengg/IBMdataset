n=int(input())
dict={}
res=[]
for i in range(n):
    ss=input().split()
    if ss[0]=='insert':
        dict[ss[1]]=i
    elif ss[0]=='find':
        if dict.__contains__(ss[1]):
            res.append('yes')
        else:
            res.append('no')
    
for i in res:
    print(i)
    
