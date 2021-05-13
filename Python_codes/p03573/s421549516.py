n = list(map(int,input().split()))
s = list(set(n))
a = n.count(s[0])
if a == 1:
    print(s[0])
else:
    print(s[1])