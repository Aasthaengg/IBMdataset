N, K = map(int, input().split())
S = list(input())

# 初期の幸福度を計算
h = 0

for i in range(1, N):
    if S[i - 1] == S[i]:
        h += 1
        
# 基本的には１操作につき幸福度は2上がる

h += 2 * K

# 幸福度がN-1を超えることはない

if h > N - 1:
    h = N - 1
    
print(h)