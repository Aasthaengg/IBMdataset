S = input()
tmp = ''.join(list(reversed(S)))
s = 0
ans = 'YES'

for i in range(len(S)):
    if tmp[s:i] == 'maerd' or tmp[s:i] == 'remaerd'or tmp[s:i] == 'esare' or tmp[s:i] == 'resare':
        s = i
        ans = 'YES'
        continue
    
    if len(tmp[s:i]) > 7:
        ans = 'NO'
        break
        
print(ans)