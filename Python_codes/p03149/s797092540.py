a,b,c,d = map(int, input().split())
l = [a,b,c,d]
ll = [1,9,7,4]
l.sort()
ll.sort()
if l == ll:
    print("YES")
else:
    print("NO")