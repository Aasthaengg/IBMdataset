s=input();w=int(input());ans=[]
while len(s)>0:
  ans.append(s[:w][0])
  s=s[w:]
print("".join(ans))