#coding:UTF-8

n = input()
ans='' #初期化
for i in range(3,n+1):
    if i%3 == 0 or '3' in str(i): #in演算子で3があるか判定
        ans +=' '+str(i)
print ans