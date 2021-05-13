N = int(input())
p = list(map(int, input().split()))
count = 0
i = 0

while N > i:
    if p[i]-1 == i:
        count += 1
        i += 1
    i+=1
print(count)
