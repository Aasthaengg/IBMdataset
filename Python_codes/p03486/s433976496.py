s = list(input())
t = list(input())

s.sort()
t.sort()
t.reverse()

if(s<t):
    print("Yes")
else:
    print("No")