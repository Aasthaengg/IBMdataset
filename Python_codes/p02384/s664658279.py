class Dice:
    def __init__(self,t,f,r,l,ba,bo):
        self.t = t
        self.f = f
        self.r = r
        self.l = l
        self.ba = ba
        self.bo = bo

s = input().split(" ")
dice = Dice(s[0],s[1],s[2],s[3],s[4],s[5])
n = int(input())
for i in range(n):
    t = input().split(" ")
    if t[0] == dice.t:
        if t[1] == dice.f:
            print(dice.r)
        elif t[1] == dice.r:
            print(dice.ba)
        elif t[1] == dice.ba:
            print(dice.l)
        else:
            print(dice.f)
    elif t[0] == dice.f:
        if t[1] == dice.bo:
            print(dice.r)
        elif t[1] == dice.r:
            print(dice.t)
        elif t[1] == dice.t:
            print(dice.l)
        else:
            print(dice.bo)
    elif t[0] == dice.r:
        if t[1] == dice.bo:
            print(dice.ba)
        elif t[1] == dice.t:
            print(dice.f)
        elif t[1] == dice.f:
            print(dice.bo)
        else:
            print(dice.t)
    elif t[0] == dice.l:
        if t[1] == dice.bo:
            print(dice.f)
        elif t[1] == dice.t:
            print(dice.ba)
        elif t[1] == dice.f:
            print(dice.t)
        else:
            print(dice.bo)
    elif t[0] == dice.ba:
        if t[1] == dice.bo:
            print(dice.l)
        elif t[1] == dice.t:
            print(dice.r)
        elif t[1] == dice.r:
            print(dice.bo)
        else:
            print(dice.t)
    elif t[0] == dice.bo:
        if t[1] == dice.f:
            print(dice.l)
        elif t[1] == dice.l:
            print(dice.ba)
        elif t[1] == dice.r:
            print(dice.f)
        else:
            print(dice.r)