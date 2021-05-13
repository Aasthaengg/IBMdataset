h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))
aa=[]

for index,item in enumerate(a):
    for _ in range(item):
        aa.append(index+1)


result=[[0]*w for _ in range(h)]

#aの位置を示す
i=0

for y in range(h):
    for x in range(w):
        #偶数段は左向き、奇数段は右向き
        if y%2==0:
            result[y][x]=aa[i]
        else:
            result[y][w-1-x]=aa[i]
        i+=1

for item in result:
    print(" ".join(map(str,item)))