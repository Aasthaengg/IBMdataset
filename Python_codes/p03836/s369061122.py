sx, sy, tx, ty = map(int, input().split())
mx = tx - sx
my = ty - sy
print("U"*my+"R"*mx+"D"*my+"L"*mx+"L"+"U"*(my+1)+"R"*(mx+1)+"DR"+"D"*(my+1)+"L"*(mx+1)+"U")
