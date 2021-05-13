import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

N,M = MI()
AB = [tuple(MI()) for _ in range(N)]
AB.sort()

ans = 0
i = 0
while M > 0:
    A,B = AB[i]
    if M >= B:
        ans += A*B
        M -= B
        i += 1
    else:
        ans += A*M
        break
print(ans)
