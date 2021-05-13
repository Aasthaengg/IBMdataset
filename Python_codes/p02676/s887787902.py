K = int(input())
S = input()
o = S if len(S) <= K else S[:K]+'...'
#このスライス忘れたらあかんよーーーー
print(o)
