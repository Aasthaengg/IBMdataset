S = list(input())
N = int(input())

'''
ordの位置
#z = 122
#a = 97
左の文字からNで'a'に出来るかを確認
aに出来るならaにして使った分をNから引く
繰り返して行き一番最後にあまりをすべて使う
'''
  
for i, s in enumerate(S):
  if ord(s) - 97 > 0  and 122 - ord(s) < N:
    S[i] = "a"
    N -= 123 - ord(s)
else:
  S[i] = chr(N % 26 + ord(S[i])) # ここのWAは反省する
       
print("".join(S))