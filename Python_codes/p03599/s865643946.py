a,b,c,d,e,f = map(int, input().split())


maxab = f //100
maxcd = f*e //(100+e)

res =[]

for i in range(maxab//a +1):
    for j in range(maxab//b +1):
        wa = a*i + b*j
        if 0 < wa*100 < f:
            for k in range(maxcd//c +1):
                for l in range(maxcd//d +1):
                    su = c*k + d*l
                    if (su <= wa*e) and wa*100+su <= f:
                        g = su/(wa*100+su)
                        res.append([g,wa*100+su,su])
        else:
            pass

resr = sorted(res,key=lambda x: x[0], reverse=True)

print(resr[0][1],resr[0][2])