N, M = map(int, input().split())
ans = set(range(1,M+1))
for i in range(N):
    A = set(map(int, input().split()[1:]))
    ans = ans&A
#    print(ans)
#    print(i)
print(len(ans))
