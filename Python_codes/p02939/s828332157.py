s = input()
n = len(s)
ans = 1
l = ''
k = s[0]
for i in range(1,n):
    
    
    if l + s[i] != k :
        k =  l + s[i] 
        l =''
        ans += 1
    else:
        l += s[i]
print(ans)