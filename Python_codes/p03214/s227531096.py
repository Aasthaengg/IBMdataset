N = int(input())
a = list(map(int, input().split()))

dif = 100
mean_a = sum(a)/len(a)
for i in range(len(a)):
  if abs(a[i]-mean_a) < dif:
    ans = i
    dif = abs(a[i]-mean_a)

print(ans)