n = int(input())
a = list(map(int,input().split()))
to = abs(a[0]) + abs(a[-1])

for i in range(n-1):
    to += abs(a[i] - a[i+1])

print(to - abs(a[0]) - abs(a[0]-a[1]) + abs(a[1]))
for i in range(1,n-1):
    print(to - abs(a[i-1] - a[i]) - abs(a[i] - a[i+1]) + abs(a[i-1] - a[i+1]))
print(to - abs(a[-2]-a[-1]) - abs(a[-1]) + abs(a[-2]))