n=int(input())

l=[int(x) for x in input().split()]

m=l.pop(l.index(max(l)))

if m<sum(l):
    print("Yes")
else:
    print("No")
