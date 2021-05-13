N, C, K = map(int,input().split())
T = []
ans = 0 #バス内の人数
num = 1 #バスの台数
for i in range(N):
    ans = int(input())
    T.append(ans)
T = sorted(T)
ans = 0
S =  T[0] + K #バスの発車時刻
for i in T:
    if i <= S and ans < C:
        ans += 1
    else:
        num += 1
        S = i + K
        ans = 1
print(num)
