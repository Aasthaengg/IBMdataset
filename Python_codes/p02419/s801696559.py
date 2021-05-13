ans=[]
W=raw_input()
while True:
    i = raw_input()
    if i == 'END_OF_TEXT': break
    ans+=[j.lower() for j in i.split()]
print ans.count(W)
