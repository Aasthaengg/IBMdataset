N = int(input())
A_s = list(map(int, input().split()))

sunuke = A_s[0]
kuma = sum(A_s[1:])
mini = abs(sunuke - kuma)


for i in range(1, N - 1):
    sunuke += A_s[i]
    kuma -= A_s[i]
    
    mini = min(mini, abs(sunuke - kuma))

print(mini)