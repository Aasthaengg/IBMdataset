n, a, b, c, d = map(lambda x:int(x)-1,input().split())
n += 1
S = input()

ok = True
overtake = False

if c < d:
    overtake = True
    
for i in range(a,d):
    if S[i] == "#" and S[i+1] == "#":
        ok = False

for i in range(b,min(d+1,n-1)):
    if S[i] == "." and S[i-1] == "." and S[i+1] == ".":
        overtake = True
        
if ok and overtake:
    print('Yes')
else:
    print('No')