n=int(input())
for _ in range(n):
    a,b,c=sorted([int(i) for i in input().split()])
    print("YES" if c**2==a**2+b**2 else "NO")
