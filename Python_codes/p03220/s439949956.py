N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
tans = 1000
nans = 0
for i in range(N):
    ans = abs(A - (T - (H[i] * 0.006)))
    if ans == 0:
        print(i+1)
        exit()
    elif ans < tans:
        tans = ans
        nanns = i
print(nanns+1)
