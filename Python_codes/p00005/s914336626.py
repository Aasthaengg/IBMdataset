# coding: utf-8
#Problem Name: GCD and LCM
#ID: tabris
#Mail: t123037@kaiyodai.ac.jp

while True:
    try:
        a,b = map(int,raw_input().split(' '))
        s,t = a,b
        while True:
            r = s % t
            if not r:
                LCM = t
                break
            else:
                s,t = t,r
        
        print LCM, a*b/LCM
    except:
        break