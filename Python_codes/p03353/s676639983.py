s = input()
K = int(input())

se = set()
for L in range(1,K+1):
  for i in range(len(s)):
    se.add(s[i:i+L])

    
li = list(se)
li.sort()
print(li[K-1])
