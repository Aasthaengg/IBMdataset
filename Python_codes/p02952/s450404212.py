# coding: utf-8
# Your code here!

n = int(input())

count = 0
for i in range(n):
    j = i + 1
    
    if len(str(j)) % 2 == 1:
        count += 1
        
print(count)