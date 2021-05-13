S = int(input())
ten = len(str(S))-1
if S <= 10**9:
    print(S,0,1,1,0,0)
else:
    t = int(str(S)[-10::-1][::-1])+1
    if S == 10**18:
        t -= 1
    print(t,1,t*10**9-S,10**9,0,0)