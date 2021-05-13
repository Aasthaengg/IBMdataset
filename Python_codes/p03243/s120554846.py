n = int(input())

while True:
    n_s = str(n)
    if n_s[0] == n_s[1] == n_s[2]:
        break
    
    n += 1
    
print(n)