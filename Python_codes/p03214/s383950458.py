# 第5回 ドワンゴからの挑戦状 予選: A – Thumbnail
N = int(input())
a = [int(i) for i in input().split()]

avg = sum(a) / len(a)
diff = [abs(i - avg) for i in a]

print(diff.index(min(diff)))