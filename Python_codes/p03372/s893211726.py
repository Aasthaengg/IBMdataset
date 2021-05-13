N,C = map(int,input().split())
XV = [[0,0]] + [[int(i) for i in input().split()] for _ in range(N)] + [[C,0]]

Sum_left = [0] * (N+1)
Sum_right = [0] * (N+1)
for i in range(N):
    Sum_left[i+1] = Sum_left[i] + XV[i+1][1]
    Sum_right[i+1] = Sum_right[i] + XV[N-i][1]

Sum_right_maxA = [0] * (N+1)
Sum_right_maxB = [0] * (N+1)
for i in range(1,N+1):
    Sum_right_maxA[i] = max(Sum_right_maxA[i-1], Sum_right[i] - 2 * (C - XV[N+1-i][0]))
    Sum_right_maxB[i] = max(Sum_right_maxB[i-1], Sum_right[i] - (C - XV[N+1-i][0]))

ans = 0
for i in range(N+1):
    ans = max(ans, Sum_left[i] + Sum_right_maxA[N-i] - XV[i][0], Sum_left[i] + Sum_right_maxB[N-i] - 2*XV[i][0])
print(ans)
