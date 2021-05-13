n = int(input())
s = 0

for i in range(1, n+1):
    y = n//i
    s += i*y*(y+1)//2
    
print(s)