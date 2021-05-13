N = int(input())
A = list(map(lambda x: int(x) -1, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

cnt = 0
prev_food = -10
for a in A:
    cnt += B[a]
    if prev_food == a-1:
        cnt += C[a-1]
    prev_food = a
print(cnt)