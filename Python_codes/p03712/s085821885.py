H,W = map(int,input().split())
a = [input() for h in range(H)]

for h in range(H+2):
  if h==0 or h==H+1:
    print((W+2)*"#")
  else:
    print("#"+a[h-1]+"#")