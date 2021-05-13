n = int(input())
h = list(map(int, input().split()))

higher = [0]
move = [0]

for i in range(1, n):
  if h[i-1] < h[i]:
    m = i - higher[len(higher) - 1] - 1
    move.append(m)
    higher.append(i)

move.append(len(h) - 1 - higher[len(higher) - 1])


print(max(move))