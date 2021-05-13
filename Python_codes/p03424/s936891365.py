N = int(input())
S = input()
for i in range(N):
  if S[2 * i] == "Y":
    print("Four")
    break
  if i == N - 1:
    print("Three")