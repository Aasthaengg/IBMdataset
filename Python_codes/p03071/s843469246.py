A, B = map(int,input().split())

#A,Bに対し、得られるコインの枚数はCOIN１、COIN2、COIN３の３パターンあり、その中で最大値を表示したい

COIN1= A+B
COIN2=A + A-1
COIN3=B + B-1
#print(COIN1) 
#print(COIN2)
#print(COIN3)

if COIN1>= COIN2 and COIN1 >= COIN3:
        print(COIN1)
elif COIN2 >=COIN1 and COIN2 >= COIN3:
    print(COIN2)
elif COIN3 >= COIN1 and COIN3 >=COIN2:
    print(COIN3)
