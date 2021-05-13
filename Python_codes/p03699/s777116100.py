n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))

l.sort()
ans = sum(l)
if ans%10 != 0:
    print (ans)
    exit ()
else:
    for i in l:
        tmp = ans - i
        if tmp%10 != 0:
            print (tmp)
            exit ()
print (0)
