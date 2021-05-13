n = int(input())
import sys

a = 0
s = []
fl = 0
for i in range(1,500):
    a += i
    s.append(a)
    
for i in range(len(s)):
    if s[i] == n:
        fl = 1
        leng = i+1
        
if fl == 0:
    print("No")
    sys.exit()
    
print("Yes")
print(leng+1)
ans = [[] for _ in range(leng)]
a = 0

for i in range(leng):
    while True:
        a += 1
        ans[i].append(a)
        if len(ans[i]) == i+1:
            break
            
for j in range(leng-1,-1,-1):
    a = ans[j][len(ans[j])-1]
    for k in range(leng-1-j):
        a += (k + j + 1)
        ans[j].append(a)
        
sime = s[:leng]
nn = len(ans[0])

for i in range(leng):
    print(nn,*ans[i])
    
print(nn,*sime)