s = input()[::-1]
t = input()[::-1]

for i in range(len(s) - len(t) + 1):
    check = True
    for j in range(len(t)):
        if s[i+j] == t[j]:
            pass
        elif s[i+j] == "?":
            pass
        else:
            check = False
            break
        
    if check:
        s = list(s)
        t = list(t)
        s[i:i+len(t)] = t
        s = "".join(s)
        s = s.replace("?","a",50)
        print(s[::-1])
        exit()
            
print("UNRESTORABLE")
            

