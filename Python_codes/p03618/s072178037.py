A = input()

dic = {}
for i in range(len(A)):
    if A[i] in dic:
        dic[A[i]] += 1
    else:
        dic[A[i]] = 1

ans = len(A)*(len(A)-1)//2 + 1
for key in dic:
    ans -= dic[key]*(dic[key]-1)//2

print(ans)