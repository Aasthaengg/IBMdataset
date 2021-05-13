a,b,c,d,e,f=map(int,input().split())

if a>b:
    a, b = b, a

ans1 = a*100
ans2 = 0
    
flag = True

for _a in range(f//(a*100) + 1):
    for _b in range((f - _a*100)//(b*100) + 1):
        for _c in range((f - _a*100 - _b*100)//c + 1):
            for _d in range((f - _a*100 - _b*100 - _c * c)//d + 1):
                if a*100*_a+b*100*_b+c*_c+d*_d == 0:
                    continue                
                if a*100*_a+b*100*_b+c*_c+d*_d > f:
                    continue  
                    
                if (c*_c+d*_d)/(a*100*_a+b*100*_b+c*_c+d*_d) == e/(100+e):
                    print(a*100*_a+b*100*_b+c*_c+d*_d, c*_c+d*_d)
                    flag = False
                    break
                elif (c*_c+d*_d)/(a*100*_a+b*100*_b+c*_c+d*_d) > e/(100+e):
                    continue
                else:
                    if ans2/ans1 < (c*_c+d*_d)/(a*100*_a+b*100*_b+c*_c+d*_d):
                        ans1 = a*100*_a+b*100*_b+c*_c+d*_d
                        ans2 = c*_c+d*_d
            if flag:
                continue
            else:
                break
        if flag:
            continue
        else:
            break
    if flag:
        continue
    else:
        break

else:
    print(ans1, ans2)
