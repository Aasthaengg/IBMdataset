N = int(input())
for l in range(N):
    a = [int(i) for i in input().split()]
    a.sort()
    if a[0]*a[0] + a[1]*a[1] == a[2]*a[2]:
        print("YES")
    else:
        print("NO")
