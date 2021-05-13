s = str(input())
k = int(input())



num = 1


for i in range(len(s)):
    ind = i+1
    if s[i] != '1':
        num = int(s[i])
        break
        
if k>= ind:
    ans = num
else:
    ans = 1
    
print(ans)