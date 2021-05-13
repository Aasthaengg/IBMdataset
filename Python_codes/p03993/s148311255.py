N = int(input())
*a, = map(int, input().split())

count = 0
for i in range(N):
    # print(a[a[i]-1])
    if i + 1 == a[a[i]-1]:
        count += 1

print(count//2)