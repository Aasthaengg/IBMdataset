n,m = map(int,input().split())
A = [int(i) for i in input().split()]
A.sort()
CB = []
for i in range(m):
   b,c = map(int,input().split())
   CB.append([c,b])
CB.sort(reverse=True)
ans = sum(A)
index = 0
for c,b in CB:
    for i in range(b):
        if index >=n:
            print(ans)
            exit()
        if A[index] < c:
            ans += c-A[index]
            A[index] = c
            index += 1
        else:
            print(ans)
            exit()
print(ans)

