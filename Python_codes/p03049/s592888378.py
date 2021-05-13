
N = int(input())
xa= 0
bx= 0
ba = 0
ans = 0
for i in range(N):
    s = input()
    ans += s.count("AB") # くっつけなくても見つかるABのカウント
    if s[-1] == "A" and s[0] == "B":
        ba += 1
    elif s[-1] == "A":
        xa+= 1
    elif s[0] == "B":
        bx+= 1

hoge  = "X"
PHASEA = 0
PHASEB = 1
phase  = 0
while ba != 0 or xa != 0 or bx != 0:
    if hoge[-1] == "X":
        if xa > 0:
            xa  -= 1
            hoge += "XA"
        elif ba > 0 :
            ba -= 1
            hoge += "BA"
        else:
            bx -= 1
            hoge += "BX"
    elif hoge[-1] == "A":
        if ba > 0 :
            ba -= 1
            hoge += "BA"
        elif bx > 0:
            bx  -= 1
            hoge += "BX"
        elif xa > 0:
            xa  -= 1
            hoge += "XA"

print(hoge.count("AB") + ans)


