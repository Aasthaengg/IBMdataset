SA = list(input())
SB = list(input())
SC = list(input())
j = 0
turn = 'a'
a = 1
b = 1
c = 1


while j == 0:
    if(turn == 'a' and len(SA) >= a):
        turn = SA[a-1]
        a += 1
    elif(turn == 'b' and len(SB) >= b):
        turn = SB[b-1]
        b += 1
    elif(turn == 'c' and len(SC) >= c):
        turn = SC[c-1]
        c += 1
    elif(turn == 'a' and len(SA) < a):
        turn = 'a'
        j = 1
    elif(turn == 'b' and len(SB) < b):
        turn = 'b'
        j = 1
    elif(turn == 'c' and len(SC) < c):
        turn = 'c'
        j = 1
        
if(turn == 'a'):
    print('A')
elif(turn == 'b'):
    print('B')
elif(turn == 'c'):
    print('C')