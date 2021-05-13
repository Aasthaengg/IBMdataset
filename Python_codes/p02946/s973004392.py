K, X = map(int, input().split())
Ans = []
for k in range(X-(K-1), X+K):
  Ans.append(str(k))
Answer = " ".join(Ans)
print(Answer)