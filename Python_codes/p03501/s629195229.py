N,A,B=map(int,input().split()) #1行で1スペースあけて入力


price1=A*N
price2=B

if price1>=price2:
    print(int(price2))
else:
    print(int(price1))
