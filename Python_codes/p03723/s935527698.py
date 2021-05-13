A,B,C=map(int,input().split())
ans=0

if A%2!=0 or B%2!=0 or C%2!=0:
      pass
elif A==B and B==C:
  ans=-1
else:
  while True:
    if A%2!=0 or B%2!=0 or C%2!=0:
      break

    A,B,C=B/2+C/2,A/2+C/2,A/2+B/2
    ans+=1

print(ans)