a,b,x = [int(x) for x in input().split()]

# a + b = x
# x - a = b

if (x - a) >= 0 and (x - a) <= b:
    print("YES")
else:
    print("NO")