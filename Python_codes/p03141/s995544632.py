
N = int(input())

ab = [tuple(map(int,input().split())) for _ in range(N)]

diff = sorted(((a+b,a,b) for a,b in ab), reverse=True)

print(sum(a for _,a,b in diff[::2]) - sum(b for _,a,b in diff[1::2]))