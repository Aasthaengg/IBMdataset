n = int(input())
s = list(input())

import collections
c = collections.Counter(s)

ans = c["R"] * c["B"] * c["G"]

for i in range(n-2):
    for j in range(i+1,n-1):
        x = s[i]
        y = s[j]
        
        if x != y:
            if "R" not in [x,y]:
                if 2*j-i < n:
                    if s[2*j-i] == "R":
                        ans -= 1
                    
            elif "G" not in [x,y]:
                if 2*j-i < n:
                    if s[2*j-i] == "G":
                        ans -= 1
                    
            else:
                if 2*j-i < n:
                    if s[2*j-i] == "B":
                        ans -= 1
    
print(ans)