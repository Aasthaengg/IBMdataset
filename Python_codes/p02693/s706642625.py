k = int(input())
a,b = list(map(int,input().split()))

s = a//k
t = b//k
if s != t:
    ans = True
elif a % k == 0:
    ans = True
else:
    ans = False

print("OK" if ans else "NG")
