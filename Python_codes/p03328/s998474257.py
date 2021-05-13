a,b = (int(T) for T in input().split())
Left = 0
Right = 1
for Leng in range(1,1000):
    Left += Leng
    Right += Leng+1
    if (Right-Left)==(b-a):
        print(Left-a)
        break