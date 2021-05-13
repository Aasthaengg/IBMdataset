n, q = map(int, input().split())
s = input()
keep = [0]*(n)

for i in range(1, n):
    keep[i] = keep[i-1]
    l, r = i-1, i+1
    if s[l:r] == "AC":
        keep[i] += 1

for j in range(q):
    l, r = map(int, input().split())
    print(keep[r-1]-keep[l-1])
