# coding: utf-8
# Your code here!
R, G, B, N = list(map(int, input().split()))

answer = 0
for r in range(N//R + 1):
    for g in range((N - r*R)//G + 1):
        if (N-r*R-g*G) % B == 0:
            answer += 1

print(answer)