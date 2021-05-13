import re

S = input()
T = input()

flag = False
for i in range(len(S) - len(T), -1, -1):
    pattern = S[i:i+len(T)].replace('?', '.')
    m = re.search(pattern, T)
    if m:
        # result = re.sub(pattern, T, S)
        result = S[:i] + T + S[i+len(T):]
        flag = True
        break

if flag > 0 :
    output = result.replace('?', 'a')
    
else :
    output = 'UNRESTORABLE'
    
print(output)
