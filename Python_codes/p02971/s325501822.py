import copy
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
c = a.count(max(a))
a_2 = copy.copy(a)
t = max(a)

if c > 1:
    for i in range(n):
        print(t)
else:
    a_2.remove(t)
    t_2 = max(a_2)
    for i in a:
        if i == t:
            print(t_2)
        else:
            print(t)
