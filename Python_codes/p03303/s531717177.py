S = input()
w = int(input())
output = ""
for i in range(len(S)):
  if i % w == 0:
    output = output + S[i]
    
print(output)
