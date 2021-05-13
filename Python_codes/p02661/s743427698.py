n = int(input())
A = [[int(i) for i in input().split(" ")] for j in range(n)]
a = sorted([i[0] for i in A])
b = sorted([i[1] for i in A], reverse=True)
if n%2 == 1:
    print(b[n//2]-a[n//2]+1)
else:
    l = (a[n//2-1] + a[n//2]) / 2
    r = (b[n//2-1] + b[n//2]) / 2
    print(int((r-l)*2)+1)