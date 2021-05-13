N, K, Q = map(int, input().split())
participant_score = [K] * N
for i in range(Q):
    A_i = int(input())
    participant_score[A_i - 1] += 1
[print('Yes' if participant_score[i] - Q > 0 else 'No') for i in range(N)]
