#B
import math
S = str(input())
w = int(input())
L = len(S)
ans = ""
for i in range(math.ceil(L/w) ):
    ans+=S[w*i]
    
print(ans)

