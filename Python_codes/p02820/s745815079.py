janken = {"r": "p",
          "s": "r",
          "p": "s"}


n, k = [int(i) for i in input().split()]
r, s, p = [int(i) for i in input().split()]
T = list(input())
score = {"r": r,
         "s": s,
         "p": p}

ans = 0
for i in range(n):
    if i < k:
        ans += score[janken[T[i]]]
    else:
        if T[i] == T[i - k]:
            T[i] = "-"
        else:
            ans += score[janken[T[i]]]
print(ans)
