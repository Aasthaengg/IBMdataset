import random
D = int(input())
C = list(map(int, input().split()))
S = list(map(int, input().split()) for _ in range(D))

ans = [0]*D
for i in range(D):
    ans[i] = random.randint(1,26)

print("\n".join(map(str, ans)))