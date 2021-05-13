import sys
k = int(input())
a,b = map(int,input().split())
for m in range(1000):
    if a <= m*k <= b:
        print("OK")
        sys.exit()
print("NG")