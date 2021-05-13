#n , m , l = map(int , input().split())

# list_n = list(map(int , inpuut().split()))<Paste>

#n = input()
# list = [input() for i in range(N)

#list = [[i for i in range(N)] for _ in range(M)]


N, M, C = map(int, input().split())
list_B = list(map(int, input().split()))
ans = 0
for Ni in range(N):
    list_A = list(map(int, input().split()))
    temp = 0
    for Mi in range(M):
        temp += list_A[Mi]*list_B[Mi]
    temp = temp + C
    if temp > 0:
        ans += 1
print(ans)
