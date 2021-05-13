n = int(input())
l = list(map(int, input().split()))
maxl = max(l)
l.remove(maxl)
if  sum(l) > maxl:
    print("Yes")
else:
    print("No")