import sys

X = int(input())
# 例外処理
if X < 400 or X >= 2000:
    print("error") 
    sys.exit()

# 級の境界値とXを比較
for score, kyu in zip(reversed(range(400, 2000, 200)), range(1, 9)):
    if X >= score:
        print(kyu)
        break