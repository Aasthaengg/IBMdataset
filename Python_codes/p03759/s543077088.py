import sys
a,b,c = list(map(int, input().split()))
print("YES" if b*2 == a+c else "NO")