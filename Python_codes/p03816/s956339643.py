n = int(input())
a = list(map(int, input().split()))
a.sort()
count = 0
for i in range (0,len(a)-1):
    if (a[i] == a[i+1]):
        count += 1
if (count % 2 == 1):
    print(len(a)-count-1)
else:
    print(len(a)-count)