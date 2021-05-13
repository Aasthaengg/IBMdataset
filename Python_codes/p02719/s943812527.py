n, k = map(int, input().split())
w = n%k
w2 = abs(w-k)
if w > w2:
    print(w2)
else:
    print(w)