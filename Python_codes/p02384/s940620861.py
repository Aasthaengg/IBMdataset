ls = list(map(int,input().split()))
q = int(input())
a = [[ls[1],ls[2]],[ls[2],ls[4]],[ls[4],ls[3]],[ls[3],ls[1]]]
b = [[ls[5],ls[2]],[ls[3],ls[5]],[ls[0],ls[3]],[ls[2],ls[0]]]
c = [[ls[5],ls[4]],[ls[1],ls[5]],[ls[0],ls[1]],[ls[4],ls[0]]]
d = [[ls[5],ls[1]],[ls[4],ls[5]],[ls[0],ls[4]],[ls[1],ls[0]]]
e = [[ls[2],ls[5]],[ls[0],ls[2]],[ls[3],ls[0]],[ls[5],ls[3]]]
f = [[ls[2],ls[1]],[ls[4],ls[2]],[ls[3],ls[4]],[ls[1],ls[3]]]
for i in range(q):
    K = list(map(int,input().split()))
    if K in  a:
        print(ls[0])
    elif K in b:
        print(ls[1])
    elif K in c:
        print(ls[2])
    elif K in d:
        print(ls[3])
    elif K in e:
        print(ls[4])
    elif K in f:
        print(ls[5])
