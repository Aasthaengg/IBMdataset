a,b,c = [int(x) for x in input().rstrip().split()]
if b-a == c-b:
    print("YES")
else:
    print("NO")