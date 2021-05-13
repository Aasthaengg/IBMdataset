n = int(input())
a, b = map(int, input().split())
P = list(map(int, input().split()))

fst, snd, thr = 0, 0, 0

for p in P:
    if p <= a:
        fst += 1
    elif a + 1 <= p <= b:
        snd += 1
    else:
        thr += 1

print(min([fst, snd, thr]))