N = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

score_a = a[::2]
score_b = a[1:][::2]

print(sum(score_a) - sum(score_b))
