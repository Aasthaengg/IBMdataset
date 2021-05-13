N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
diff_list = []
for i in range(N):
  tmp = T - H[i]*0.006
  diff = abs(A-tmp)
  diff_list.append(diff)
ans = diff_list.index(min(diff_list)) + 1
print(ans)