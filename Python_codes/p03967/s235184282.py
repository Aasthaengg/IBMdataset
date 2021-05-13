#D問題
import math
S = list(str(input()))
N = len(S)

count = 0
n = math.ceil(N/2)
for i in range(N):
    if i < n:
        if S[i] == "p":
            count-=1
    else:
        if S[i] == "g":
            count+=1
            
print(count)