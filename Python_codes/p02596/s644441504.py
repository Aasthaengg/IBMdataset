K = int(input())
count = 1
mod = 7
answer = -1

for _ in range(K):
    if mod % K == 0:
        answer = count
        break
    count += 1
    mod = (mod * 10 + 7) % K

print(answer)