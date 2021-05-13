X = int(input())
acc = 0
# X > 0 なのでマイナス方向にジャンプする選択肢は選ばない
for i in range(X + 1):
    acc += i
    if X <= acc:
        ans = i
        break
print(i)
