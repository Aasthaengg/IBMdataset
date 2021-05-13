n = int(input())

t = 0
    
while t*111 < n  and n > (t+1)*111:
    t += 1
    
print((t+1)*111)