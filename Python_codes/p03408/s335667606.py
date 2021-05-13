
import collections

N=input()

N=int(N)

aaa=[]

for i in range(N):
    a1=input()
    aaa.append(a1)


M=input()

M=int(M)


bbb=[]

for i in range(M):
    a1=input()
    bbb.append(a1)
    
#print(aaa)

#print(bbb)


c = collections.Counter(aaa)

d = collections.Counter(bbb)

#print(c)

#print(d)

#print(c-d)

dic2 = sorted((c-d).items(), key=lambda x:x[1], reverse=True)


#print(len(dic2))

if len(dic2)==0:
    print(0)
else:
    print(dic2[0][1])
