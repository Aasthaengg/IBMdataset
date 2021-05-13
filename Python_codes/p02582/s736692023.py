S = str(input())

if S[0]=='S' and S[1]=='S' and S[2]=='S':
  sum = 0
elif (S[0]=='R' and S[1]=='R' and S[2]=='S') or (S[0]=='S' and S[1]=='R' and S[2]=='R'):
  sum = 2
elif S[0]=='R' and S[1]=='R' and S[2]=='R':
  sum = 3
else:
  sum = 1
  
print(sum)