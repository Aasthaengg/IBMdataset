# 1番目はコスト0
# 2番目は |A2 - A1|
# 3番目は |A3 - A2|
a,b,c = sorted(map(int, input().split()))
print(abs(b-a)+ abs(c-b))