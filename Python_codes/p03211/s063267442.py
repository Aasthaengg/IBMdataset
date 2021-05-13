S=input()
mini=1000

for i in range(0,len(S)-2):
  i1=int(S[i])
  i2=int(S[i+1])
  i3=int(S[i+2])
  x=i1*100+i2*10+i3
  if abs(x-753)<mini:
    mini=abs(x-753)

print(mini)