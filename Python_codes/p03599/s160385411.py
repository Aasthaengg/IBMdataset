A,B,C,D,E,F=map(int, input().split())

#A,B　水
#C,D satou
#E 溶解度　F 容量

V=0
node=0
total=0
sugar=0

for a in range(F//(100*A)+1):
    for b in range((F-100*A*a)//(100*B)+1):
        v=F-100*A*a-100*B*b
        for c in range(v//C+1):
            v2=v-c*C
            for d in range(v2//D+1):
                v3=v2-d*D
                if v3<0:
                    continue
                if a==0 and b==0:
                    continue
                if (c*C+d*D)/(a*A+b*B)>E:
                    continue
                nownode=100*(c*C+d*D)/(F-v3)
                if nownode>=node:
                    node=nownode
                    total=F-v3
                    sugar=(c*C+d*D)

print(total, sugar)
