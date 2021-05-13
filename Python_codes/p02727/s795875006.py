import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


X,Y,A,B,C = MI()
P,Q,R = LI(),LI(),LI()

Z = [(P[i],1) for i in range(A)] + [(Q[i],0) for i in range(B)] + [(R[i],-1) for i in range(C)]
Z.sort(reverse=True)
a,b,c = 0,0,0  # 選択した赤リンゴ、緑リンゴ、無色リンゴの個数
n = 0  # 選択したリンゴの個数
ans = 0
for x in Z:
    if n == X+Y:
        break
    s,t = x
    if t == 1 and a == X:
        continue
    elif t == 0 and b == Y:
        continue
    else:
        n += 1
        ans += s
        if t == 1:
            a += 1
        elif t == 0:
            b += 1
        else:
            c += 1

print(ans)
