N = int(input())
As = list(map(int,input().split()))
count = 0
while all(a%2==0 for a in As):
  As = [a/2 for a in As]
  count = count + 1
print(count)