N = int(input())

ans = 10**9+7

allN = 10**N #全ての整数の列
left = 9 ** N #左端が0か9
right = 9 ** N #右端が0か9
ryoutan = 8 ** N #両端0か9

ncc =  allN - left - right + ryoutan
print(int(ncc%ans))