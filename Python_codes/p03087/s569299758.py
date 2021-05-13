n,q = map(int,input().split())
s = input()
ac = [0] * (n+1)
num = 0

for i in range(n):
    if i != 0:
        if s[i-1:i+1] == "AC":
            num += 1
            
    ac[i+1] = num
    
for i in range(q):
    l,r = map(int,input().split())
    print(ac[r]-ac[l])