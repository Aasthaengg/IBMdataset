s = list(input())
K = int(input())

i = 0
while(s[i]=='1'):
    K -= 1 
    if K == 0:
        break 
    i += 1 
print(s[i])
