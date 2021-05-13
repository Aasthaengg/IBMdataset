S = input()
ans = 0
nd = 1
mod1 = 0
listmod = [0]*2019
for i in S[::-1]:
    mod1 = (int(i)*nd + mod1)%2019
    listmod[mod1] += 1
    nd = (nd*10)%2019
for i in range(2019):
    n = listmod[i]
    if(i == 0):
        if(n == 1):
            ans += 1
        elif(n >= 2):
            ans += ((n+1)*n)//2
    else:
        if(n > 1):
            ans += ((n-1)*n)//2
print(ans)