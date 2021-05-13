S = str(input())
w = int(input())
N = len(S)
roop = int((N-1)/w+1)
ans = []
for i in range (roop):
  ans.append(S[i*w])
Ans =''.join(ans)
print(Ans)