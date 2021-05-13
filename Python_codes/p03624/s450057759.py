S = list(input())
Sd = {i:S[i] for i in range(len(S))}
check = {i:0 for i in range(26)}
ans = -1

for k,v in Sd.items():
    check[ord(v)-ord('a')] = 1
    
for k,v in check.items():
    if v == 0:
        ans = k
        break
        
if ans == -1:
    print('None')
else:
    print(chr(ans+ord('a')))