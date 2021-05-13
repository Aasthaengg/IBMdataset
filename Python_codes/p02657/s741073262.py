def main():
  l = input().split()
  A, B = int(l[0]), float(l[1])
  B100 = int(B*1000)
  ans = int((A*B100)/1000)
  print(ans)
  return

main()