# coding: utf-8
# Your code here!
s = input().split()
n = int(s[0])#price
m = int(s[1])#num of kind

coins = input().split()


min_count = [99999 for i in range(n)]

for j in range(m):
    coins[j] = int(coins[j])
    
for i in range(n):
    buf = 99999
    if i+1 in coins:
        min_count[i] = 1
        continue
    for j in coins:
        if i<j: continue
        buf = min(buf,min_count[i-j]+1)
    min_count[i] = buf
    
print(min_count[n-1])
