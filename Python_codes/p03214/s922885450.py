n = int(input())
a = list(map(int, input().split()))
 
ave = sum(a) / n
hantei = 200000
ans = 0
for i, f in enumerate(a):
    if hantei > abs(ave - f):
        hantei = abs(ave - f)
        ans = i
 
print(ans)