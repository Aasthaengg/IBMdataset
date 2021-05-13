N, W = map(int, input().split())
V = [[] for i in range(4)]
w0, v0 = map(int, input().split())
V[0].append(v0)
for i in range(N - 1):
  w, v = map(int, input().split())
  V[w - w0].append(v)
V = [[0] + sorted(V[i], reverse=True) for i in range(4)]
value = 0
val = [0] * 4
for i in range(min(W // w0 + 1, len(V[0]))):
  val[0] += V[0][i]
  for j in range(min((W - w0 * i) // (w0 + 1) + 1, len(V[1]))):
    val[0] += V[1][j]
    val[1] += V[1][j]
    for k in range(min((W - w0 * (i + j) - j) // (w0 + 2) + 1, len(V[2]))):
      val[0] += V[2][k]
      val[2] += V[2][k]
      for l in range(min((W - w0 * (i + j + k) - j - k * 2) // (w0 + 3) + 1, len(V[3]))):
        val[0] += V[3][l]
        val[3] += V[3][l]
      value = max(value, val[0])
      val[0] -= val[3]
      val[3] = 0
    val[0] -= val[2]
    val[2] = 0
  val[0] -= val[1]
  val[1] = 0
print(value)