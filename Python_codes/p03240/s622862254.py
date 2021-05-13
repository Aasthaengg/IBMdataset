n=int(input())
l=[list(map(int,input().split())) for i in range(n)]

for x in range(101):
    for y in range(101):
        k=set(e+abs(x-q)+abs(w-y)  for q,w,e in l if e)
        for pre in k:
            for a,s ,d in l:

                if d!=max(0,pre-abs(x-a)-abs(s-y)):break
            else:print(x,y,pre);exit()