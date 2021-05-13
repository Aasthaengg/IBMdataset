N = int(input())
A = list(map(int,input().split()))

dic = {}
for i in range(N):
    data = A[i]
    if data in dic:  dic[data] += 1
    else:  dic[data] = 1
        
ans = 0
for i in dic:
    if dic[i] > i:  ans += dic[i] - i
    elif dic[i] < i:  ans += dic[i]
print(ans)