N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input() + "0"*K
#T = T.replace("r",P).replace("s",R).replace("p",S)
#print(T)
#rn, sn, pn = 0, 0, 0
r, s, p = 0, 0, 0

for i in range(N):
    i = int(i)
    if T[i] == T[i+K]:
        T = T[:i+K] + "0" + T[i+K+1:]
        """
        if T[i] == "r":
            rn += 1


        elif T[i] == "s":
            sn += 1

        else:
            pn += 1
        """
    else:
        if T[i] == "r":
            r += 1

        elif T[i] == "s":
            s += 1

        elif T[i] == "p":
            p += 1

#for i in [rn, sn, pn,r, s, p]:
    #print(i)
#sum = P*(r+(rn//2)) + R*(s+(sn//2)) + S*(p+(pn//2))
#print(T)
sum = P*T.count("r") + R*T.count("s") + S*T.count("p")
print(sum)