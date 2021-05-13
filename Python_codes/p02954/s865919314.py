S = list(input())
ans = [0]*len(S)
R = 1
r = 0
L = 0
l = 0
for i in range(1,len(S)):
  if S[i-1] == "R" and S[i-1] == S[i]:
    R += 1
  elif S[i-1] == "R" and S[i] == "L":
    L += 1
    r = i-1
    l = i
  elif S[i-1] == "L" and S[i] == "L":
    L += 1
  elif (S[i-1] == "L" and S[i] == "R"):
    ans[r] += (R+1) //2 + L//2
    ans[l] += R //2 + (L+1)//2
    R = 1
    L = 0
  if i == len(S)-1:
    ans[r] += (R+1) //2 + L//2
    ans[l] += R //2 + (L+1)//2
    
print(*ans)
    
  
  
