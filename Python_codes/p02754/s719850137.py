N, A, B = map(int,input().split())

if A == 0:
    print(0)
    exit()

s = N // (A+B)
p = N%(A+B)
if p//A == 0:
    ans = s*A+p
else:
    ans = s*A+A
print(ans)
