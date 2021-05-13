s = input()
l = list(set(s))

if len(set(s)) == 1:
    print(0)
    exit()

min_c = 10**8
for i in l:
    old_s = s
    new_s = ''
    idx = 1
    c = 0
    
    while True:
        for j in range(len(s)-idx):
            if old_s[j] == i or old_s[j+1] == i:
                new_s += i
            
            else:
                new_s += old_s[j]
        
        idx += 1
        c += 1
        
        if len(set(new_s)) == 1:
            break
        
        else:
           old_s = new_s
           new_s = ''
    
    min_c = min(min_c,c)

print(min_c)