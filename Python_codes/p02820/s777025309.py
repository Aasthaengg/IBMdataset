n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = input()
li = [[""]*((n+k)//k) for i in range(k)]
for i in range(n):
    li[i%k][i//k] = t[i]
ans = 0
for i in li:
    P,R,S = 0,0,0
    hand_o = ""
    for j in i:
        if j == "r" and hand_o != "r":
            P += p
        elif j == "s" and hand_o != "s":
            R += r
        elif j == "p" and hand_o != "p":
            S += s
        else:
            hand_o = ""
            continue
        hand_o = j
    ans += (P+R+S)
print(ans)