#testB
if __name__=="__main__":
  r, g, b = map(int, input().split())
  k = int(input())


  for _ in range(k):
      if not r < g:
        g = g*2
        continue
      if not g < b:
        b = b*2
        use = False
  if r < g and g < b:
    print("Yes")
  else:
    print("No")
