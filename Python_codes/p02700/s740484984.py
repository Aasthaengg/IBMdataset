import math
a,b,c,d = map(int,input().split())

t_turn = math.ceil(c/b)
a_turn = math.ceil(a/d)

if t_turn <= a_turn:
    print("Yes")
else:
    print("No")