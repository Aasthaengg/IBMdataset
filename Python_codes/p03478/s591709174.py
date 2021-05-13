import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

N,A,B = MI()

ans = 0
for i in range(1,N+1):
    if A <= sum(int(j) for j in list(str(i))) <= B:
        ans += i
print(ans)
