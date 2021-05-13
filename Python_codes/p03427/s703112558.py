n = list(str(input()))
maxi = 0
#print(n)
for i in range(len(n)):
  #print(int(n[i])-1, int(n[i])-1 + (len(n)-i-1)*9)
  maxi = max(maxi, int(n[i])-1 + (len(n)-i-1)*9)
print(max(sum(map(int, n)), maxi))