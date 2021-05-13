n=int(input())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]
a.reverse()
b.reverse()
sum=0
for a,b in zip(a,b):
  a+=sum
  sum+=(b-(a%b))%b
print(sum)