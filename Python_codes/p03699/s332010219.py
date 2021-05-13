n = int(input())
s1 = [int(input()) for i in range(n)]
total = sum(s1)
if total%10 != 0:
    print(total)
else:
    s1.sort()
    s2=[s for s in s1 if s%10!=0]
    if s2:
        print(total-s2[0])
    else:
        print(0)
