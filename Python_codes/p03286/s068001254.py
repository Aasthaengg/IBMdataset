N = int(input())
ans = []
while N != 0:
    if  N % 2 != 0:
        N -= 1
        ans.append("1")
    else:
        ans.append("0")
    N //= -2

if ans:
    print("".join(reversed(ans)))
else:
    print("0")