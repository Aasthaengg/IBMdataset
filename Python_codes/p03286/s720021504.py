N = int(input())
if N == 0:
    print("0")
else:
    ans = []
    p = 1
    while 2**(p-1) <= abs(N):
        if N%(2**p) > 0:
            ans.append("1")
            N -= (-2)**(p-1)
        else:
            ans.append("0")
        p += 1

    print("".join(ans[::-1]))
