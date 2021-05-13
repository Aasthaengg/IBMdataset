N = int(input())
ans = 0
if N == 1:
    ans = 1
elif N%2 != 1:
    ans= 0.5
else:
    ans=(N+1)/(2*N)
print(ans)