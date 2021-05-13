N, K, Q = map(int, input().split())
answered = [0] * N
passed = 0

for i in range(Q):
    who = int(input())
    answered[who-1] += 1

for point in answered:
    if point > Q - K:
        print('Yes')
    else:
        print('No')
