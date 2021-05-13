from collections import Counter
n = int(input())
d= Counter(list(map(int, input().split())))
m = int(input())
t= Counter(list(map(int, input().split())))
if t-d=={}:
    print("YES")
else:
    print("NO")
