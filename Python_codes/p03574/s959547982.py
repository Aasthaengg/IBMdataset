h,w=map(int,input().split())
s = [["."for i in range(w+2)]]
for i in range(h):s.append(["."]+list(input())+["."])
s.append(["."]*(w+2))
l=[]
for i in range(1,h+1):
 l2=[]
 for j in range(1,w+1):
  if s[i][j]=="#":l2.append("#")
  else:l2.append(str([s[i+1][j],s[i+1][j+1],s[i+1][j-1],s[i][j+1],s[i][j-1],s[i-1][j-1],s[i-1][j],s[i-1][j+1]].count("#")))
 l.append("".join(l2))
print(*l,sep="\n")