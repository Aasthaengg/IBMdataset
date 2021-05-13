n = int(input())
l = list( map(int,input().split()))
m = max(l)
s = sum(l)
if 2*m < s:
    print("Yes")
else:
    print("No")