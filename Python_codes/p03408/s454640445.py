import collections

n = int(input())
blue = []
for i in range(n):
    blue.append(input())

red = []   
m = int(input())
for i in range(m):
    red.append(input())
    
b1 = collections.Counter(blue)
r1 = collections.Counter(red)

ans = 0

for key, value in b1.items():
    if key in r1:
        tmp = b1[key] - r1[key]
        ans = max(ans, tmp)
    else:
        ans = max(ans, b1[key])
        
print(ans)