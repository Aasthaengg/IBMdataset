S=input()
N=len(S)
r_S=S[::-1]
c1=int((N-1)/2)
c2=int((N+3)/2)
S1=S[:c1]
r_S1=S1[::-1]
S2=S[(c2-1):]
r_S2=S2[::-1]


#kaibun hantei
if S==r_S and S1==r_S1 and S2==r_S2:
  print("Yes")
else:
  print("No")