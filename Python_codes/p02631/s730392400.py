N = int(input())
a = list(map(int,input().split()))

S=a[0]
for i in range(1,len(a)):
  S ^= a[i]

ans = []
for i in range(len(a)):
  ans.append(str(S^a[i]))
print(' '.join(ans))