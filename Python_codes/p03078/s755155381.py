X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
E = []
for a in A:
    for b in B:
        E.append(a + b)
E.sort(reverse=True)
E = E[:K]
ans = []
for e in E:
    for c in C:
        ans.append(e + c)
ans.sort(reverse=True)
ans = ans[:K]
for x in ans:
    print(x)