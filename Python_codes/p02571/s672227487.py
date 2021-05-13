S=input()
T=input()

max_ans=0
for i in range(len(S)):
  max_n = 0
  for j in range(len(T)):
    if len(S) >= i + len(T):
      if S[i+j]==T[j]:
      	max_n=max_n+1
  
  if max_ans <= max_n:
    max_ans=max_n

print(len(T)-max_ans)