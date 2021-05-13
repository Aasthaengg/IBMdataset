a, b, k = map(int, input().split())
ll = []
for i in range(k):
    if a+i <= b:
        ll.append(a+i)
for j in range(k):
    if not b-k+j+1 in ll and b-k+j+1>=a:
        ll.append(b-k+j+1)
for k in ll:
    print(k)
