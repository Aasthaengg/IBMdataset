A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0

for a in range(A+1):
    value = X-a*500
    if value == 0:
        count += 1
        continue
    for b in range(B+1):
        value = X-a*500-b*100
        if value == 0:
            count += 1
            continue
        for c in range(C+1):
            value = X-a*500-b*100-c*50
            if value == 0:
                count += 1

print(count)
