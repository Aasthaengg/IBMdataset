N = int(input())
A,B,C = [input() for _ in range(3)]

answer = 0
for a,b,c in zip(A,B,C):
  answer += len(set([a,b,c])) - 1

print(answer)