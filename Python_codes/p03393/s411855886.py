alp = "abcdefghijklmnopqrstuvwxyz"
s = input()
if len(s) < 26:
    for x in alp:
        if x not in s:
            print(s+x)
            break
elif s == alp[::-1]:
    print(-1)
else:
    # ここから
    for i in range(24,-1,-1):
        for j in range(25,i,-1):
            #print(i,j,s[i],s[j])
            if s[i] < s[j]:
                print(s[:i] + s[j])
                exit()
