n = int(input())
a = list(map(int, input().split()))
count = 0
counter = 0

for i in range(len(a)-1):
    if i == len(a)-2 and a[i]==a[i+1]:
        count += int((i+2-counter)//2)
    if a[i]!=a[i+1]:
        count += int((i+1-counter)//2)
        counter = i + 1

print(count)      