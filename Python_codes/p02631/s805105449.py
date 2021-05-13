n = int(input())
a_list = list(map(int, input().split()))
base_xor = 0
for i in a_list:
    base_xor = base_xor^i
ans = [0]*n
for i in range(n):
    ans[i] = a_list[i]^base_xor
ans = " ".join([str(i) for i in ans])
print(ans)