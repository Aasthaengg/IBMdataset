n = int(input())

a = []
m = 101
c = 0
for i in range(n):
    tmp = int(input())
    if tmp%10 != 0:
        c += 1
        m = min(tmp,m)
    a.append(tmp)

if sum(a)%10 != 0:
    print(sum(a))
elif sum(a)%10 == 0 and c == 1:
    print(m)
elif sum(a)%10 == 0 and c == 0:
    print(0)
else:
    print(sum(a)-m)






