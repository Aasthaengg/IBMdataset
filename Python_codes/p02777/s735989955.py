s = input().split()
a,b = map(int,input().split())
u = input()
if u==s[0]:
    print(a-1,b)
else:
    print(a,b-1)