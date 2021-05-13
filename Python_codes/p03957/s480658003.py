s = input()
n = len(s)

def solve() :
  for i in range(n) :
    for j in range(i + 1, n) :
      if s[i] == 'C' and s[j] == 'F' :
        return 'Yes'
    
  return 'No'
      
print(solve())