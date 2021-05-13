n = int(input())
li_a = list(map(int, input().split()))

ave = sum(li_a) / n
minimum = min(abs(ave - a)for a in li_a)

for idx, v in enumerate(li_a):
    if abs(ave - v) == minimum:
        print(idx)
        exit(0)
