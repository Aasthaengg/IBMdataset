n = int(input())
a = list(map(int, input().split()))
aset = len(set(a))
if aset%2 == 0:
    print(aset-1)
else:
    print(aset)