MAX_B = 10**5
N = int(input())
B = [MAX_B] + list(map(int, input().split())) + [MAX_B]
res = 0
for i in range(N):
    res += min(B[i], B[i + 1])
print(res)