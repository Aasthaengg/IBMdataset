s = input()
q = int(input())

f1 = 1
f2 = 2
cnt = 0
st = ""
se = ""

for _ in range(q):
    q = input().split()
    if int(q[0]) == 1:
        cnt += 1
    elif int(q[0]) == 2:
        if cnt % 2 == 0:
            if int(q[1]) == 1:
                st = q[2] + st
            elif int(q[1]) == 2:
                se += q[2]
        else:
            if int(q[1]) == 1:
                se += q[2]
            elif int(q[1]) == 2:
                st = q[2] + st


ans = st + s + se
if cnt % 2 == 0:
    print(ans)
else:
    ans = list(ans)
    ans.reverse()
    ans = "".join(ans)
    print(ans)