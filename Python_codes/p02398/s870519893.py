divisors = []
divisorsc = []

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

for n in range(int(c)):
    if c%(n + 1) == 0:
        divisorsc.append(n+1)

#if a == b:
    #if a in divisorsc:
       # divisors.append(a)
        
for i in range(1 + b - a):
    if i + a in divisorsc:
        divisors.append(i+a)
        
print(len(divisors))