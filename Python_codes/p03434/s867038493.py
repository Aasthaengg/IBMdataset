N = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
answer = 0
for i in range(0,N,2):
  answer += a[i]
for i in range(1,N,2):
  answer -= a[i]
print(answer)