S = input()

S_midn = int(len(S) / 2)
S_rev = S[::-1]
count = 0

for i in range(S_midn):
  if S[i] != S_rev[i]:
    count += 1
    
print(count)
#print(S, S_rev, S_midn)