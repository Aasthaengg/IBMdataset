# 136 B - Uneven Numbers
N = int(input())
counter = 0
for i in range(N,0,-1):
    if(len(str(i))%2==1):
        counter += 1
print(counter)