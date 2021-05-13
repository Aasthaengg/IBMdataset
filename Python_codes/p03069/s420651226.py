n = int(input())
s = input()

kuro_li = [0]*(n+1)

if s[0] == "#":
    kuro_li[1] = 1

for i in range(1,n):
    #print(i)
    kuro_li[i+1] = kuro_li[i]
    if s[i] == "#":
        kuro_li[i+1] += 1
        
siro_li = [0]*(n+1)

if s[-1] == ".":
    siro_li[-2] = 1

for i in range(n,0,-1):
    #print(i)
    siro_li[i-1] = siro_li[i]
    if s[i-1] == ".":
        siro_li[i-1] += 1
    
#print(kuro_li)
#print(siro_li)


ans = 10**10

for i in range(n+1):
    tmp = kuro_li[i] + siro_li[i]
    ans = min(ans,tmp)
    
print(ans)