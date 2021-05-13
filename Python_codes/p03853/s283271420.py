H, W = map(int, input().split())

output = []
for _ in range(H):
  S = input()
  output.append(S)
  output.append(S)

print(*output, sep='\n')
