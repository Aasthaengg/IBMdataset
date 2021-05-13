b=input()

#Alphabetの互換性を関連付ける
#片方だけでは正しく出力しない
a={"A":"T", "T":"A", "C":"G", "G":"C"}

#abが逆ではErrorが発生する
print(a[b])