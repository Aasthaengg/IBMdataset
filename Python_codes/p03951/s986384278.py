import sys
n = int(input())
pre = input()
suf = input()
if pre==suf:
    print(n)
    sys.exit()
slicer, ans = n-1 , n*2
for xx in range(n+1):
    if suf[:slicer] in pre:
        ans = len(pre)+(len(suf)-len(suf[:slicer]))
        break
    slicer-=1
print(ans)