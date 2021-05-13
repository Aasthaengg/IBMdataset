import sys

N = int(input())
a = list(map(int, input().split()))
ans = 0 
count = 1
if 1 not in a :
    print(-1)
    sys.exit()

for i in range(N) :
    if a[i] == count :
        count += 1
    else :
        ans += 1
print(ans)
