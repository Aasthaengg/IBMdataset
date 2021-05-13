n=int(input())
al=['a','b','c','d','e','f','g','h','i','j','k']
a=[['a',0]]
b=[]
for k in range(n-1):
    for i in a:
        for j in range(i[1]+2):
            b.append([i[0]+al[j],max(i[1],j)])
    a=b
    b=[]
a.sort(key=lambda x:x[0])
for i in a:
    print(i[0])