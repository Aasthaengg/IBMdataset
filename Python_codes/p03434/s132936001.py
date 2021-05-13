#B - Card Game for Two 〇
N = int(input())
a = list(map(int,input().split()))

a = sorted(a, reverse = True)

score = 0
for i in range(N):
    if i % 2 == 0:
        score += a[i]
    else:
        score -= a[i]
print(score)