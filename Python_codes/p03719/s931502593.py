# coding: utf-8
# Your code here!
line = input().split()
l = [int(s) for s in line]

# print(l)

a = 0 

if -100 <= l[0] <= l[2] <= l[1]<=100:
    a = 1
    
    
if a == 1 :
    print("Yes")
    
else:
    print("No")