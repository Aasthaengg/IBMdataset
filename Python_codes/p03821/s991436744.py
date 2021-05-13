import sys
input = sys.stdin.buffer.readline

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
A = [AB[i][0] for i in range(N)]
B = [AB[i][1] for i in range(N)]

ans = 0
for i in reversed(range(N)):
    ans += (-(-(A[i]+ans)//B[i]) * B[i]) - (A[i] + ans)

print(ans)