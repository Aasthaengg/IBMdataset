S = input()
T = input()

answer = 0
for s,t in zip(S,T):
    if s is t: answer += 1

print(answer)
