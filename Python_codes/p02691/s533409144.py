N = int(input())
A = list(map(int, input().split()))

I = [i+a for i,a in enumerate(A, start=1)]
J = [i-a for i,a in enumerate(A, start=1)]
#print(I, J)

dic = {}
ans = 0

for i in range(N):
    if I[i] in dic:
        dic[I[i]] += 1
    else:
        dic[I[i]] = 1
    if J[i] in dic:
        ans += dic[J[i]]


#print(dic)
print(ans)
