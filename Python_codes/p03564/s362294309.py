s = input()
v = input()

n = int(s)
k = int(v)

x = 1

for i in range(n):
    x = min(x * 2,x + k)
    
print(x)