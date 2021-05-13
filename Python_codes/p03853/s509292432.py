h,w = map(int,input().split())

output = []
for _ in range(h):
  s = input()
  output.append(s)
  output.append(s)

print(*output,sep='\n')