N = int(input())
A = list(map(int, input().split()))
cnt = 0
for a in A:
    while a % 2 == 0:
        cnt += 1
        a /= 2
print(cnt)
# Aのそれぞれの要素の2で割り切れる回数の和