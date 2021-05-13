n = int(input()) 
a = [input() for _ in range(n)] 
b = [0,0,0,0] 
c = ["AC","WA","TLE","RE"]

for i in range(len(c)): 
    for k in range(n): 
        if a[k] == c[i]:
           b[i] += 1

for i in range(len(c)): 
    print(c[i]+" x "+str(b[i]))