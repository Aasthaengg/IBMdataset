def main():
  H,W = map(int,input().split())
  _a = [input() for _ in range(H)]
  a =["#"*(W+2)]*(H+2)
  for i in range(H):
    a[i+1] = "#" + _a[i] + "#"
  for i in range(H+2):
    print(a[i])

main()  