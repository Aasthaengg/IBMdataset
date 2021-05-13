s = input()
s1 = s.replace("A","")

t = "KIHBR"

if ("AI" in s) or ("AH" in s) or ("RAA" in s):
    print("NO")
    exit()
    
a = 0
for i in range(len(s)):
    if s[i] == "A":
        a +=1
    elif s[i] != "A":
        if a > 1:
            print("NO")
            exit()
        a = 0
  
if s1 == t:
    print("YES")
else:
    print("NO")