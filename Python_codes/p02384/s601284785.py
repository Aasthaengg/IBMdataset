class dice:
    def __init__(s, i):
        s.d1,s.d2,s.d3,s.d4,s.d5,s.d6 = map(int, i)
        s.dic = {s.d1:{s.d2:s.d3,s.d3:s.d5,s.d4:s.d2,s.d5:s.d4}
                ,s.d2:{s.d1:s.d4,s.d3:s.d1,s.d4:s.d6,s.d6:s.d3}
                ,s.d3:{s.d1:s.d2,s.d2:s.d6,s.d5:s.d1,s.d6:s.d5}
                ,s.d4:{s.d1:s.d5,s.d2:s.d1,s.d5:s.d6,s.d6:s.d2}
                ,s.d5:{s.d1:s.d3,s.d3:s.d6,s.d4:s.d1,s.d6:s.d4}
                ,s.d6:{s.d2:s.d4,s.d3:s.d2,s.d4:s.d5,s.d5:s.d3}}
 
    def get(s, i):
        up, bef = map(int, i)
        return s.dic[up][bef]

dice1 = dice(input().split())
q = int(input())
for i in range(q):
    print(dice1.get(input().split()))
    
