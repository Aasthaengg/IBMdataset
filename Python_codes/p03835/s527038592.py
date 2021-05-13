import sys

k,s = map(int,sys.stdin.readline().split(' '))

result = 0

for x in range(k+1):
    for y in range(k+1):
        z = s-x-y
        if z < 0: continue
        if z<=k:
            result+=1
        
print(result)