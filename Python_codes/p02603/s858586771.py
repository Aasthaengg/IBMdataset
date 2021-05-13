import sys
imput = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

money = 1000

for i in range(N-1):
  if a[i+1] > a[i]:
    k = money//a[i]
    money += a[i+1]*k - a[i]*k
    
print(money)