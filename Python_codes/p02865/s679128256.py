# -*- coding: utf-8 -*-

def main():
  inline = [input() for i in range(1)]
  outline = 0

  try:
    wk_inline = int(inline[0])
  except Exception as e:
    print('整数値を入力してください')
    return 0

  if wk_inline % 2 == 0:
      outline = wk_inline //2 -1
  else:
      outline = wk_inline // 2

  print(outline)
  return 0

main()