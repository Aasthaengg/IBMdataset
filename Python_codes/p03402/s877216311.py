A,B = map(int, input().split())

# でかいブロック分だけ引いておく
A,B = A-1,B-1
ANS = []
def calc(X):
  if X>49:
    X -= 49
    wk = 49
  else:
    wk = X
    X = 0
  return X,wk

while A > 0:
  ANS.append("#"*100)
  A,wk = calc(A)
  ANS.append("#" + ".#" * wk + "##" * (49-wk) + "#")
  A,wk = calc(A)
  ANS.append("#" + "#." * wk + "##" * (49-wk) + "#")
ANS.append("#"*100)
while B > 0:
  ANS.append("."*100)
  B,wk = calc(B)
  ANS.append("." + ".#" * wk + ".." * (49-wk) + ".")
  B,wk = calc(B)
  ANS.append("." + "#." * wk + ".." * (49-wk) + ".")
ANS.append("."*100)

print(len(ANS), 100)
for a in ANS:
  print("".join(a))
  
"""
こう言うブロックを繰り返すと、３−４行で98分離成分が稼げる
100/2= 50行あれば、A、BのMAX500は稼げる。構築する
####################
#.#.#.#.#.#.#.#.#.##49
##.#.#.#.#.#.#.#.#.#49
####################
"""
