S = input()
if len(S) <26:
    for i in range(97,97+26):
        if chr(i) in S:
            continue
        else:
            print(S+chr(i))
            exit()
else:
    for i in range(25,0,-1):
        s =S[:i]
        for j in range(97,97+26):
            if chr(j)>s[-1] and chr(j) not in s:
                print(s[:-1]+chr(j))
                exit()
print(-1)
                
        
