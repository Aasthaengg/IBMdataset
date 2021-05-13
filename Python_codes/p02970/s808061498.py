N, D = map(int, input().split())

if N % (2*D+1) == 0:
    ans = N // (2*D+1)
else:
    ans = (N // (2*D+1))+1

print(ans)
