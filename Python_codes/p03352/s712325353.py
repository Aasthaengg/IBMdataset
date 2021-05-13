X = int(input())

l = [1]

for b in range(2,32):
    p = 2
    while b**p <= X:
        l.append(b**p)
        p +=1
        
print(max(l))