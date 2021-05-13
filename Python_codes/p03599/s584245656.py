a,b,c,d,e,f = map(int, input().split())
s = [0,0,0,0]
con1 = 0
for x in range(31):
    for y in range(31):
        for v in range(1501):
            if x == y == 0:
                continue
            else:
                w1 = (f-(100*a*x + 100*b*y + c*v))//d
                w2 = (100*a*x + 100*b*y -c*v)//d
                w3 = ((100*a*x + 100*b*y)*e -c*v*100)//(100*d)
                w = min(w1,w2,w3)
                con2 = 100*(c*v + d*w)/(100*a*x + 100*b*y +c*v +d*w)
                if con1 <= con2 and w >= 0:
                    con1 = con2
                    s = [x,y,v,w]
                else:
                    continue

ans1 = 100*a*s[0] + 100*b*s[1] + c*s[2] + d*s[3]
ans2 = c*s[2] + d*s[3]
print(ans1,ans2)