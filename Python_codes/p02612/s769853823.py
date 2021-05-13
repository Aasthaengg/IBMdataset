# coding: utf-8
# Your code here!
n = int(input())

while True:
    if n <= 1000:
        ans = 1000 - n
        break
    n -= 1000
    
print(ans)