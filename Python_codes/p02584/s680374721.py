X, K, D = list(map(int, input().split()))

X = abs(X)
count = X // D

if count >= K:
    answer = X - K*D
else:
    if (K - count) % 2 == 0:
        answer = X - count*D
    else:
        answer = abs(X - (count+1)*D)

print(answer)