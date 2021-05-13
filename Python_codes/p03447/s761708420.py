X,A,B = [int(input()) for i in range(3)]
#ケーキを買ったあと
amari = X - A 
#ドーナツ買ったあまり
print(amari % B)