n = int(input())
s = input()

def Z_algo(S):
    n = len(S)
    LCP = [0]*n
    i = 1
    j = 0
    c = 0
    for i in range(1, n):
        if i+LCP[i-c] < c+LCP[c]:
            LCP[i] = LCP[i-c]
        else:
            j = max(0, c+LCP[c]-i)
            while i+j < n and S[j] == S[i+j]: j+=1
            LCP[i] = j
            c = i
    LCP[0] = n
    return LCP
  
ans = 0
for i in range(n):
  z = Z_algo(s[i:])
  for i,zi in enumerate(z):
    ans = max(ans,min(i,z[i]))
    
print(ans)