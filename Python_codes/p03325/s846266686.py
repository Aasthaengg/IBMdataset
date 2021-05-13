N = int(input())
A = list(map(int,input().split()))
B = []
count = 0
for a in A:
    if a % 2 == 0:
        B.append(a)

for i in B:
    while i % 2 == 0:
        i = i / 2
        count += 1

print(count)