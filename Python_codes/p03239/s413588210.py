T, N = list(map(int,input().split()))

ans_c = 1001
for i in range(T):
    c, t = list(map(int,input().split()))
    if (N >= t) and (c <= ans_c):
        ans_c = c

if ans_c == 1001:
    print("TLE")
else:
    print(ans_c)