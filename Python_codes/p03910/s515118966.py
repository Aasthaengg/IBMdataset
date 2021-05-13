n = int(input())
x = int(n**0.5)
while x*(x+1)//2 < n:
    x += 1
skip = x*(x+1)//2 - n
for i in range(1,x+1):
    if skip != i: print(i)