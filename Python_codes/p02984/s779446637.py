n = int(input())
a_list = list(map(int, input().split()))
x = sum(a_list[::2]) - sum(a_list) // 2
ans = []
for a in a_list:
    ans.append(str(x * 2))
    x = a - x
print(' '.join(ans))