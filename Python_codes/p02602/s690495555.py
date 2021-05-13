n, k = map(int, input().split())
a_i = list(map(int, input().split()))
for x in range(n - k):
    if a_i[x] < a_i[x + k]: print("Yes")
    else: print("No")