count = 0
num = int(input())
p = list(map(int, input().split()))

for i in range(len(p)-2):
    q = sorted(p[i:i+3])

    if q[1] == p[i+1]:
        count += 1
        
print(count)