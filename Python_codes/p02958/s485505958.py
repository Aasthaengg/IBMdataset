n = int(input())
p = list(map(int,input().split()))

a = [i for i in range(1,n+1)]

c = 0
for i in range(n) :
    if a[i] != p[i] :
        c += 1
print("YES" if c<=2 else "NO")
