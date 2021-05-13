def main():
  s=input()
  sa=int(s[:2])
  sb=int(s[2:])
  if 1 <= sa and sa <= 12:
    if 1 <= sb and sb <= 12:
      print('AMBIGUOUS')
    else:
      print('MMYY')
  else:
    if 1 <= sb and sb <= 12:
      print('YYMM')
    else:
      print('NA')
main()