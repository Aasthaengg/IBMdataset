a1=int(input())
a2=input()
res1=[i for i in a2.split()]
res=[i for i in a2.split()]
for x in res:
    if int(x)<1 or int(x)>1000:
        res.remove(x)
empty=0
sum_all=0
if 1<=a1<=100:
    if len(res1)==len(res):
        for x in res:
            empty=sum_all
            sum_all=empty+(1/int(x))
        print((1/sum_all))