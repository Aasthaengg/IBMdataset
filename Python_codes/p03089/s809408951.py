N = int(input())
B = list(map(int, input().split()))

#与えられた数列から、j番目の数がjのものを削除していくのと同義
ans = []
while len(B) > 0:
    can_delete = False
    for i in range(len(B) - 1, -1, -1):
        if i + 1 == B[i]:
            ans.append(B[i])
            del B[i]
            can_delete = True
            break
    if not can_delete:
        break

if len(B) > 0:
    print(-1)
else:
    for i in ans[::-1]:
        print(i)