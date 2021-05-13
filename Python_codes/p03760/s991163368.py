O=list(input())
E=list(input())+[""]
for x,y in zip(O, E):#zipにしてあげることで自動的にOが奇数、Eが偶数の場所になる
    print(x+y,end="")#あとは順次出力