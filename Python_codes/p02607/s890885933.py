masu = int(input())
numberlist = list(map(int,input().split()))
counter = 0

for i in range(masu):
    if (i + 1) % 2 != 0 and numberlist[i] % 2 != 0:
        counter += 1
print(counter)