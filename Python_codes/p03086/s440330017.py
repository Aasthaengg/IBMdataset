S = input()

# ACGT 

num = 0
result = [0]

    
for c in S:
  if c == 'A' or c == 'C' or c == 'G' or c == 'T':
    num += 1
  else:
    result.append(num)
    num = 0
result.append(num)
    
#print(result)
print(max(result))