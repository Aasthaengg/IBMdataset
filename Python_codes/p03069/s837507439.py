n = int(input())
s = input()

num_black = 0
num_white = 0
# 該当部分を含まずに、「より左」にある黒の数
left_black = [0] * (n+1)
# 該当部分を含まずに、「より左」にある白の数
left_white = [0] * (n+1)
for i in range(n):
    if s[i] == '#':
        num_black += 1
    else:
        num_white += 1
    left_black[i+1] = num_black
    left_white[i+1] = num_white
# 該当部分を含んで、「より右」にある白の数
right_white = [0] * (n+1)
for i in range(n,-1,-1):
    right_white[i] = num_white - left_white[i]

# インデックスiから右（iを含む）は全て黒にする、として数える
ans = num_white
for i in range(n+1):
    num_to_change = left_black[i] + right_white[i]
    ans = min(ans, num_to_change)
print(ans)




