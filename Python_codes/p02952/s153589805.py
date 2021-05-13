N = int(input())

# 桁数 => 文字列に変換して、その長さを数える
ans = 0
for i in range(1, N+1):
  if len(str(i)) % 2 == 1: ans += 1
    
print(ans)