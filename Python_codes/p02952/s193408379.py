N = int(input())
count = 0
for i in range(1,N+1):
    ar = list(map(int,str(i)))
    if len(ar) % 2 != 0:
        count += 1

print(count)