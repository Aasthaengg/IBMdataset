n = int(input())

ab = [list(map(int,input().split())) for i in range(n)]

a = [i[0] for i in ab]
b = [i[1] for i in ab]

temp = 0
for i in reversed(range(n)):
    a[i] += temp
    
    if a[i] % b[i] == 0:
        continue
    
    else:
        temp += (b[i] - (a[i]%b[i]))
    
print(temp)