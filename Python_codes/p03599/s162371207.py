a,b,c,d,e,f = map(int,input().split())

a *= 100
b *= 100
ma = (f+a-1)//a
mb = (f+b-1)//b
mc = (f+c-1)//c
md = (f+d-1)//d
ans1 = ans2 = ans3 = 0
for i in range(ma+1):
    for j in range(mb+1):
        for k in range(mc+1):
            for m in range(md+1):
                s = a*i+b*j+c*k+d*m
                if  s> f:
                    break
                if (a*i+b*j)*e >= 100*(c*k+d*m):
                    if ans3 == 0:
                        ans2 = s
                        ans3 = c*k+d*m
                    else:
                        if  ans3*s < ans2*(c*k+d*m):
                            ans2 = s
                            ans3 = c*k+d*m
print(ans2,ans3)
