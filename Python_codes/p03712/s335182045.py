H,W = map(int,input().split())
print("#"*(W+2))
for h in range(H):
  line = input()
  print("#"+line+"#")
print("#"*(W+2))