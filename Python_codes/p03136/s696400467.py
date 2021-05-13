n = int(input())
l = list(map(int,input().split()))

maxl = max(l)
if sum(l) - maxl > maxl:
    print("Yes")
else:
    print("No")

