s = input()
ans = 0
tmp = ''
c = ''
for i in s:
    c += i 
    if c!=tmp:
        ans +=1
        tmp = c
        c=''
print(ans)