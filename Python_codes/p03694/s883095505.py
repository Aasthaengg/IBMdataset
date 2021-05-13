#リスト内包表記を使う場合
N=int(input())
A=[int(x) for x in input().split()]
#Aはa1-aNを含むリスト
#これはめちゃめちゃ簡単で最大値-最小値でいい

A=sorted(A)
ans=A[N-1]-A[0]
print(ans)