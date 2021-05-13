sx, sy, tx, ty = [int(w) for w in input().split()]
dx = tx-sx
dy = ty-sy
first = "U"*dy+"R"*dx+"D"*dy+"L"*dx
second = "L"+"U"*(dy+1)+"R"*(dx+1)+"D" +\
         "R"+"D"*(dy+1)+"L"*(dx+1)+"U"

print(first+second)
