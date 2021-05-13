S = input()
t = int(input())
a = ""
for i in range(len(S)):
  if i % t == 0:
    a += S[i]
    
print (a)