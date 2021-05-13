N = int(input())
s1 = []
s2 = []
 
for i in range(N):
    a = int(input())
    if a % 10 != 0:
        s1.append(a)
    else:
        s2.append(a)

if len(s1) == 0:
    print(0)
else:
    if sum(s1) % 10 == 0:
        print(sum(s1)-min(s1)+sum(s2))
    else:
        print(sum(s1)+sum(s2))