n=int(input())
s=[input() for _ in range(n)]
ans=sum([si.count('AB') for si in s])
endA=len([si for si in s if si[-1]=='A'])
startB=len([si for si in s if si[0]=='B'])
AB=len([si for si in s if si[0]=='B' and si[-1]=='A'])
if endA*startB==0:
      print(ans)
elif AB==endA and AB==startB:
      print(ans+AB-1)
else:
      print(ans+min(endA,startB))
