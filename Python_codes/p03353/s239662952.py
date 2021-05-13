s = input()
K = int(input())
l = min(len(s),K)
lis = []
for i in range(1,l+1):
  for j in range(len(s)-i+1):
    lis.append(s[j:j+i])
lis = list(set(lis))
lis.sort()
print(lis[K-1])