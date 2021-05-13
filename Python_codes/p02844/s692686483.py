N = int(input())
S = input()

A = [0]*1000 
ans = 0

for i in range(1000):
  if i < 10:
    s = '00' + str(i)
  elif i < 100:
    s = '0' + str(i)
  else:
    s = str(i)
    
  for j in range(N):
    if S[j] == s[0]:
      for k in range(j+1,N):
        if S[k] == s[1]:
          for l in range(k+1,N):
            if S[l] == s[2]:
              A[i] = 1
              break
          break
      break

print(A.count(1))