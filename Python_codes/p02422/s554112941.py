s = input()
n = int(input())
for i in range(n):
    q = input().split()
    q1 = int(q[1])
    q2 = int(q[2]) + 1
    if q[0] == "print":
        sl = list(s)
        print("".join(sl[q1:q2]))
    elif q[0] == "reverse":
        sl = list(s)
        bb = sl[q1:q2]
        bb.reverse()
        s = "".join(sl[:q1] + bb + sl[q2:])
    elif q[0] == "replace":
        sl = list(s)
        s = "".join(sl[:q1]) + q[3] + "".join(sl[q2:])

