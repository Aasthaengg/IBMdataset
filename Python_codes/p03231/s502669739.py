def gcd(a, b):
    c = a%b
    while(c != 0):
        a = b
        b = c
        c = a%b
    return b

def answer(s, t):
    a = len(s)
    b = len(t)
    if s[0] != t[0]:
        return -1
    if a < b:
        temp = a
        a = b
        b = temp
        temp = s
        s = t
        t = temp
    gcdAB = gcd(a, b)
    if gcdAB == 1:
        return a*b
    else:
        stack = 0
        sl = (gcdAB * (a//gcdAB) * (b//gcdAB))
        aJump = sl//a
        bJump = sl//b
        for i in range(b):
            if stack%aJump == 0:
                if s[stack//aJump] != t[i]:
                    return -1
            stack = bJump*(i+1)
        return sl
                

sl, tl = map(int, input().split())
s = input()
t = input()
print(answer(s, t))
