s = input()
t = input()

go = []
back = []
g = []
b = []
def has_duplicates(seq):
    return len(seq) != len(set(seq))


for i in range(len(s)):
  go.append(s[i]+t[i])
  back.append(t[i]+s[i])

go_l = set(go)
back_l = set(back)
go = list(go_l)
back = list(back_l)

#print(go)
#print(back)

for i in range(len(go)):
  g.append(go[i][0])
  b.append(back[i][0])
  
#print(g)
#print(b)
  
ansg = has_duplicates(g)
ansb = has_duplicates(b)

if ansg == True or ansb == True:
  print("No")
else:
  print("Yes")