a,b = map(int,input().split())
dum = b-a
total = 0
for i in range(dum,0,-1):
    total += i
print(total-b)