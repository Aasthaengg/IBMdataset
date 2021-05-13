n = int(input())
s = list(map(int,input().rstrip().split()))
q = int(input())
t = list(map(int,input().rstrip().split()))

count = 0
for _t in t:
    for _s in s:
        if _t == _s:
            count += 1
            break
print(count)
