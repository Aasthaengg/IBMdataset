N = int(input())
A = list(map(int, input().split()))
B = []
for a in A:
  B.append(a%4)

ans = 'No'
if B.count(0) >= B.count(1)+B.count(3):
  ans = 'Yes'
if B.count(2) == 0 and B.count(0) == B.count(1)+B.count(3)-1:
  ans = 'Yes'
print(ans)