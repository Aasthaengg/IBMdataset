H, W=map(int, input().split())
s=["#"]*(W+2)
print("".join(s))
for i in range(H):
  tmp=input()
  tmp="#"+tmp+"#"
  print(tmp)
print("".join(s))