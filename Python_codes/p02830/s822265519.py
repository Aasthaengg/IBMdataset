N = int(input())
S, T = input().split()
answer = []
for i in range(N):
    answer.append(S[i])
    answer.append(T[i])
print(''.join(answer))