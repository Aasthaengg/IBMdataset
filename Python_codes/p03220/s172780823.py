N = int(input())
T, A = map(int, input().split())
H_list = list(map(int,input().split()))
ans = 0
temp = 10 ** 6
for i in range(N):
    t = T - H_list[i] * 0.006
    a = abs(A-t)
    if a < temp:
        ans = i + 1
        temp = a
print(ans)
