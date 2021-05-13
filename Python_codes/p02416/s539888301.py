x = int(input())
while x:
    s = 0
    while x:
        s += x%10
        x//=10
    print (s)
    x = int(input())