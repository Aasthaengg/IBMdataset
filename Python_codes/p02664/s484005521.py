S = list(input())
lon = len(S)
for i in range(lon):
  if S[i] == "?":
    S[i] = "D"
 
    

T = "".join(S)
#print(T.count("D") + T.count("PD") )
print(T)