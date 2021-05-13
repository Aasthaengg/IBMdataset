N = int(input())
T, A = map(int, input().split())
near_A = 1e8
for i, H in enumerate(map(int, input().split())):
  ave_tem = T - H * 0.006
  if near_A > abs(ave_tem - A):
    near_A = abs(ave_tem - A)
    res = i + 1
print(res)