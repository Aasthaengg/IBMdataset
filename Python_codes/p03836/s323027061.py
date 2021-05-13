sx,sy,tx,ty = map(int, input().split())

first = "U"*(ty-sy) + "R"*(tx-sx)
second = "D"*(ty-sy) + "L"*(tx-sx)
third = "L" + "U"*(ty-sy+1) + "R"*(tx-sx+1) + "D"
fourth = "R" + "D"*(ty-sy+1) + "L"*(tx-sx+1) + "U"

print(first+second+third+fourth)