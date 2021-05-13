S = input()
n = len(S)

tot = 0

for i in range(2**(n-1)):
  f = S[0]
  for j in range(n-1):
       if ((i >> j) & 1):
        f += " "
       f += S[j+1]
  
  tot += sum(map(int, f.split(" ")))

print(tot)