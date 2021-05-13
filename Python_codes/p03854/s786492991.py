S = input()[::-1]
s = ""
for i in range(len(S)):
    s += S[i]
    if s in ["maerd", "remaerd", "esare", "resare"]:  s = ""    
if s == "":  print("YES")
else:  print("NO")