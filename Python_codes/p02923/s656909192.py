N = int(input())
H = list(map(int, input().split()))
answer = 0
temp = 0
for i in range(N - 1):
    if H[i] < H[i + 1]:
        answer = max(answer, temp)
        temp = 0
    else:
        temp += 1
        answer = max(answer, temp)
print(answer)
