N = int(input())
S, T = map(list, input().split())
for i in range(2 * N):
  if i % 2 == 0:
    print(S[int(i/2)],end="")
  else:
    print(T[int((i-1)/2)],end="")