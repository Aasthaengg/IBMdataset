n,x = map(int,input().split())

s = list(map(int,input().split()))

ans = 1

s.sort()

if sum(s)==x:
    print(n)
elif sum(s)<x:
    print(n-1)
else:
    if s[0]>x:
        print(0)
    else:
        for i in range(len(s)):
            if sum(s[:i]) <= x < sum(s[:i+1]):
                print(i)