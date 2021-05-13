N = int(input())
I = [0 for i in range(N)]
answer = 0
for i in range(1, N+1):
    answer += (i + (N//i) * i) * (N//i) //2
print(answer)