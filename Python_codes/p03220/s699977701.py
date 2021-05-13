N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
lst = []
for i in range(N):
    tmp = abs(A-(T - H[i] * 0.006))
    lst.append(tmp)

print(lst.index(min(lst))+1)