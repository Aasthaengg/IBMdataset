N = int(input())
A = list(map(int,input().split()))
mean_a = sum(A)/N
distance_list = [abs(a - (mean_a)) for a in A]

for i in range(N):
  if min(distance_list) == distance_list[i]:
    ans = i
    break
print(ans)