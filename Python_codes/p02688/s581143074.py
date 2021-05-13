n,k = list(map(int, input().split()))
b = [i+1 for i in range(n)]
for i in range(k):
    d = input()
    a = list(map(int, input().split()))
    for j in a:
        try:
            b.remove(j)
        except: pass
print(len(b))