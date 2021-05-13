import bisect

s=input()
t=input()

i=1
dic=[[] for _ in range(27)]
for ss in s:
    dic[ord(ss) - 97].append(i) 
    i+=1

for index,item in enumerate(dic):
    item.sort()
    dic[index]=item

posi=-1
count=0
for tt in t:
    if dic[ord(tt) - 97]==[]:
        print(-1)
        exit()
    
    r=bisect.bisect_right(dic[ord(tt) - 97],posi)

    flag=0
    if r>=len(dic[ord(tt) - 97]):
        count+=1
        posi=dic[ord(tt) - 97][0]
    else:
        posi=dic[ord(tt) - 97][r]
    
print(count*len(s)+posi)


        



