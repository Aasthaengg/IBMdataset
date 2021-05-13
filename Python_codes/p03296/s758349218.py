N = int(input())
a = list(map(int, input().split()))

count = 0
pre = False
for i in range(N-1):
    if a[i] == a[i+1]:
        if not pre:
            count += 1
            pre = True
        else:
            pre = False
    else:
        pre = False
print(count)
