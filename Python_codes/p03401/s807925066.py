N = int(input())
src = [0] + list(map(int,input().split())) + [0]
cums = [0]
for a,b in zip(src,src[1:]):
    d = abs(a-b)
    cums.append(cums[-1] + d)

ans = []
for i in range(N):
    tmp = cums[i] + abs(src[i] - src[i+2]) + cums[-1] - cums[i+2]
    ans.append(tmp)
print(*ans, sep='\n')
