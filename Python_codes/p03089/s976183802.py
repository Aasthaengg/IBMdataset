import sys
n = int(input())
b = list(map(int, input().split()))
ans = []

for i in b:
    if len(ans) >= i-1:
        ans.insert(i-1, i)
    else:
        print(-1)
        sys.exit()
for i in ans:
    print(i, sep='\n')
