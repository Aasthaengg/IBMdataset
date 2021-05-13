n = int(input())
a = list(map(int,input().split()))
cnt = 0
for i in range(len(a)):
    cnt += 1/a[i]
print(1/cnt)