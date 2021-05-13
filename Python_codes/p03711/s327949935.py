group_a=[1,3,5,7,8,10,12]
group_b=[4,6,9,11]
group_c=[2]
x,y=map(int,input().split())
for i in group_a:
    if x==i:
        x="a"
    if y==i:
        y="a"
for i in group_b:
    if x==i:
        x="b"
    if y==i:
        y="b"
for i in group_c:
    if x==i:
        x="c"
    if y==i:
        y="c"
if x==y:
    print("Yes")
else:
    print("No")