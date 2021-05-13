S = list(input())
N = len(S)
if N == 26:
    if S == list("zyxwvutsrqponmlkjihgfedcba"):
        print(-1)
    else:
        O = [0]*(N+1)
        for i in range(N):
            O[i] = ord(S[i])

        for i in range(N)[::-1]:
            co = [0]*N
            
            for j in range(1,25):

                for k in range(N):
                    co[k] = O[k]

                co[i] += j

                if co[i] > 122:
                    continue
                else:
                    if len(set(co[0:i+1])) == len(co[0:i+1]):
                        ans = co[0:i+1]
                        break

            else:
                continue
            break

        for i in range(len(ans)):
            ans[i] = chr(ans[i])

        cans = "".join(ans)
        print(cans)

else:
    #a97 z122
    O = [0]*(N+1)
    for i in range(N):
        O[i] = ord(S[i])

    for i in range(97,123):
        if i not in O:
            last = i
            break 
    
    O[N] = i

    for i in range(N+1):
        O[i] = chr(O[i])
    
    ans = "".join(O)
    print(ans)