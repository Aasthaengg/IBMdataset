N=int(input())
S=input()
RS=S[::-1]

west=[0]
east=[0]

for i in range(N):
  if S[i]=="W":
    west.append(west[-1]+1)
  else:
    west.append(west[-1])
west.append(0)

for i in range(N):
  if RS[i]=="E":
    east.append(east[-1]+1)
  else:
    east.append(east[-1])
east.append(0)
east=east[::-1]

ans=10**9
for i in range(1,N+1):
  ans=min(ans,west[i-1]+east[i+1])

print(ans)
