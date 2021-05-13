T = "AKIHABARA"

L = []
for a in range(2) :
    if a :
        sa = "A"
    else :
        sa = ""
    for b in range(2) :
        if b :
            sb = "A"
        else :
            sb = ""
        for c in range(2) :
            if c :
                sc = "A"
            else :
                sc = ""
            for d in range(2) :
                if d :
                    sd = "A"
                else :
                    sd = ""
                
                string = sa + "KIH" + sb + "B" + sc + "R" + sd
                L.append(string)

S = input()
if S in L :
    ans = "YES"
else :
    ans = "NO"
print(ans)
