N = int(input())
AB = list()
for _ in range(N):
    ab = list(map(int, input().split()))
    ab.reverse()
    AB.append(ab)
AB.sort()
#print(AB)

at = 0
flag = False

for i in range(N):
    bt = AB[i][0]
    at += AB[i][1]
    #print(at, bt)
    if at > bt:
        flag = True
        break

if flag:
    print("No")
else:
    print("Yes")
