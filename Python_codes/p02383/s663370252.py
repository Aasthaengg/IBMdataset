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
s = input()
for i in range(len(s)):
    if s[i] == "E":
        a = dice.t
        b = dice.r
        c = dice.bo
        d = dice.l
        dice.r = a
        dice.bo = b
        dice.l = c
        dice.t = d
    elif s[i] == "N":
        a = dice.t
        b = dice.f
        c = dice.bo
        d = dice.ba
        dice.ba = a
        dice.t = b
        dice.f = c
        dice.bo = d
    elif s[i] == "S":
        a = dice.t
        b = dice.f
        c = dice.bo
        d = dice.ba
        dice.f = a
        dice.bo = b
        dice.ba = c
        dice.t = d
    else:
        a = dice.t
        b = dice.r
        c = dice.bo
        d = dice.l
        dice.l = a
        dice.t = b
        dice.r = c
        dice.bo = d
print(dice.t)