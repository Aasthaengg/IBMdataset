mod = 10**9+7

n, k = map(int,input().split())
A = list(map(int,input().split()))

#ラスト一個を除く
tentou = [0]*n
for i in range(n):
    for j in range(i+1,n):
        if A[i] > A[j]:
            tentou[i] += 1

back = [0]*n
for i in range(n):
    for j in range(i+1,n):
        if A[-(j+1)] < A[-(i+1)]:
            back[-(i+1)] += 1

#print(A)         
#print(tentou)
#print(back)

wa = k*(k+1)//2

ans = (wa%mod)*sum(tentou)%mod

ans += sum(back)*(k-1)*k//2

print(ans%mod)