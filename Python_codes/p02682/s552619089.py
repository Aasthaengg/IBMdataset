A, B, C, K = map(int, input().split())
answer = 0
answer += min(A, K)
K = K - A - B
if K > 0:
    answer -= min(C, K)
print(answer)