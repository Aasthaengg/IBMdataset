A, B = map(int, input().split())

def judge(b):
  print("Yay!" if b else ":(")
  exit()

if A <= 8 and B <= 8:
  judge(1)
else:
  judge(0)