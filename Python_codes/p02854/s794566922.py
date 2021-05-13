N = int(input())
A = list(map(int, input().split()))

cumulative = [0]
for i in range(N):
    cumulative.append(cumulative[i] + A[i])
lst = []
for i in range(1, N):
    a = abs(cumulative[i] - (cumulative[-1] - cumulative[i]))
    lst.append(a)
#print(lst)
print(min(lst))