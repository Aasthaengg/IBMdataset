N = int(input())
A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))
# どのタイミングで下移動を使うかだけが重要

lst = [0]*N
for i in range(N):
    lst[i] = sum(A1[:i+1]) + sum(A2[i:])
ans = max(lst)
print(ans)
