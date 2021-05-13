H, N = map(int, input().split())
A_list = map(int, input().split())
ans = "Yes" if sum(A_list) >= H else "No"
print(ans)