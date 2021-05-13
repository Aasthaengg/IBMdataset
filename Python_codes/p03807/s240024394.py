n = int(input())
li = [int(x)%2 for x in input().split()]
if li.count(1)%2==1:
    print("NO")
else:
    print("YES")