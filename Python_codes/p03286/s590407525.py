N = int(input())

ans = []
N = -N
while N != 0:
    ans.append(N%2)
    N //= -2

if ans:
    ans.reverse()
    print(*ans, sep="")
else:
    print(0)
