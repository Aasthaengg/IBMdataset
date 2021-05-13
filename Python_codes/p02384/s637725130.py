def R(dice,U,S):
  def f(x): return str(dice.index(x))
  PAT=["12431","03520","01540","04510","02530","13421"]
  it=f(U)+f(S)
  for i in range(6):
    if PAT[i].find(it)>=0: return dice[i]

dice = map(int,raw_input().split())
for _ in [0]*int(raw_input()):
  U,S=map(int,raw_input().split())
  print R(dice,U,S)