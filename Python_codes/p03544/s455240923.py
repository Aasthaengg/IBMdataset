r = [0]*100
r[0] = 2
r[1] = 1
for i in range(2,90):
    r[i] =r[i-2] + r[i-1]
    
n = int(input())
print(r[n])