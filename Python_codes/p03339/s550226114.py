N = int(input())
S = input()

# 西端の人がリーダーの場合
temp = 0
for j in range(1, N):
    temp += (S[j] == 'E')
    ans = temp

for i in range(1, N): # 西からi番目の人がリーダーの場合
    temp -= (S[i] == 'E')
    temp += (S[i - 1] == 'W')
    ans = min(ans, temp)

print(ans)