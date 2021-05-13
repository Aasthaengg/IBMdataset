num = int(input())
pos = list(map(int,input().split()))
maxpos = max(pos)
minhealth = 1e9
count = 0
for i in range(maxpos+1):
    for j in pos:
        count += (j-i)**2
    minhealth = min(minhealth, count)
    count = 0
print(minhealth)
