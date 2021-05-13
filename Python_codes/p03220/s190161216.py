N = int(input())
T,A = map(int,input().split())
T2 = 10**9
H = list(map(int,input().split()))
for i in range(N):
    tmp = abs(A - (T - (H[i] * 0.006)))
    if(T2 >= tmp):
        ans = i + 1
        T2 = tmp
print(str(ans))