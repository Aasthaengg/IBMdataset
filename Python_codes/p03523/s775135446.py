'''
問題の条件でAを追加できるとなっているので、
A以外の文字は無関係。公式解説を読んで、
単純に、秋葉原のローマ字の文字をBitで消した文字列と
入力文字列との比較をしたが、それでは、Aと関係のない
文字を削除・追加したものもOKと判定してしまう。
秋葉原の文字列でAとなっているところに限定して
Bit探索をする。
'''
S=input()
AKI='AKIHABARA'
AKI=list(AKI)
List=[0,4,6,8]#秋葉原の文字列でAとなっている場所に着目
for i in range(1<<4):#Bit全探索
  for j in range(4):
    if i&(1<<j):#Bitが立っていれば
      AKI[List[j]]='A'#Listのj番目の文字はAにする
    else:#そうでなければ
      AKI[List[j]]=''#Aとせず、飛ばす
    if S==''.join(AKI):#上の操作で作られた文字と入力を比較
      print('YES')
      exit()
else:
  print('NO')