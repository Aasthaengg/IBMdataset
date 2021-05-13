n = int(input())
S = list(map(int,input().split()))
p = int(input())
T = list(map(int,input().split()))
count = 0

for i in T:
    for j in S:
        if i == j:
            count += 1
            break
print(count)

