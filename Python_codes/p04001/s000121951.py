S = input()
n=len(S) - 1 
shiki = ""
output = 0
for i in range(2**n):
  result = list()
  shiki = S[0]
  for j in range(n):
    if ((i>>j)&1):
      shiki = shiki + '+' + S[j+1]
    else:
      shiki = shiki + S[j+1]
  result = list(map(int,shiki.split('+')))
  for k in range(len(result)):
    output += result[k]
print(output)