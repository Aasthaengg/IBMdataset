N = int(input())
L = list(map(int, input().split()))
s = L[0]
for i in range(len(L)-1):
  s += min(L[i], L[i+1])
print(s + L[N-2])