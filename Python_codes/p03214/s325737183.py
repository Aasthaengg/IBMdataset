n = int(input())
a = list(map(int, input().split()))
aa = [i * n for i in a]
m = sum(a)
aaa = [abs(i - m) for i in aa]
mi = min(aaa)

for idx, elem in enumerate(aaa):
    if elem == mi:
        print(idx)
        exit()
