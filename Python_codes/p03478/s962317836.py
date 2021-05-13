N, A, B = map(int, input().split())
count = 0
for i in range(1,N+1):
    n = list(k for k in str(i))
    S_n = 0
    for j in n:
        S_n += int(j)
    if A <= S_n <= B:
        count += i
print(count)