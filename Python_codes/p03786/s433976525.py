n = int(input())
ai = [int(i) for i in input().split()]

ai.sort()

tmp = ai[0]
num = 0

for i in range(1,n):
    if 2*tmp >= ai[i]:
        num += 1
    else:
        num = 0
    tmp += ai[i]
        
print(num+1)