from bisect import bisect_left 
#bisect_left(a,x):a[i]>=xとなるような最小のi.
#昇順ソートされたリストaに昇順を崩さずxを挿入できる位置s(0-index)を返す.
#a=[1,3,5,7,9,11,13,15,17,19]
#s = bisect_left(a,4)
#s=2
a,b,c,d,e,f=map(int,input().split())
wa=set()
a*=100
b*=100
for i in range((f+a-1)//a+1):
    for j in range((f+b-1)//b+1):
        if 1<=i*a+j*b<=f:
            wa.add(i*a+j*b)
su=set()
e=100*e/(100+e)
x=int(f*e//100)
for i in range((x+c-1)//c+1):
    for j in range((x+d-1)//d+1):
        if i*c+j*d<=x:
            su.add(i*c+j*d)
su=sorted(list(su))
# print(wa)
# print(su)
ans=0
x,y=0,0
e+=0.001
f+=0.001
for i in wa:
    # print(i,su[bisect_left(su,f-i)-1],su[bisect_left(su,e*i/(100-e))-1])
    p=min(bisect_left(su,f-i),bisect_left(su,e*i/(100-e)))
    if p>0:
        if ans<=su[p-1]/(i+su[p-1]):
            ans=su[p-1]/(i+su[p-1])
            x,y=i,su[p-1]
print(max(x+y,a),y)