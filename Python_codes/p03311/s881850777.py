n = int(input())
a = list(map(int, input().split(' ')))
a = [a[i]-i-1 for i in range(n)]
a.sort()
if n%2 == 0:
    num = int(n/2)
    b = int((a[num-1]+a[num])/2)
    a = [abs(a[i]-b) for i in range(n)]
else:
    num = int(n/2)
    b = int(a[num])
    a = [abs(a[i]-b) for i in range(n)]
print(sum(a))