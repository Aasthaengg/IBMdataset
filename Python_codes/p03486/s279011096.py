s=list(input())
t=list(input())

s.sort()
t.sort(reverse=True)

list=[s]+[t]
list.sort()

if list[0]==t:
    print("No")
else:
    print("Yes")