n, k = map(int, input().split())
a = list(map(int, input().split()))

a = [0] + a
a.sort()
if max(a) < k:
    print("IMPOSSIBLE")
    exit()

for i in range(len(a) - 1):
    if k == a[i]:
        print("POSSIBLE")
        break
    if a[i+1] - a[i] == 0: continue 
    if k % (a[i+1] - a[i]) == 0:
        print("POSSIBLE")
        break
else:
    print("IMPOSSIBLE")