N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
answer = [abs(A - (T - (height * 0.006))) for height in H]
print(answer.index(min(answer)) + 1)
