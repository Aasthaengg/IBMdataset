n = int(input())
a = [int(i) for i in input().split()]

s = sum(a)
if s%2==1:
    print("NO")
else:
    print("YES")