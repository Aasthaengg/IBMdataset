from collections import Counter
input()
cnt=Counter(map(int,input().split()))

for v in cnt.values():
    if v>1:
        print('NO')
        break
else:
    print('YES')