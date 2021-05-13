def main():
  o = input()
  e = input()
  s=""
  for i in range(0,len(e)):
    s =s+o[i]+e[i]
  if len(o)>len(e):
    s += o[len(o)-1]
  print(s)
main()