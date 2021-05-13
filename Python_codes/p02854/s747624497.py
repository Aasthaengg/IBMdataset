n=int(input())
A =list(map(int,input().split()))
k = sum(A)/2
cnt=0
cnt2 = 0
for i in A:
    k -= i
    if k < 0:
        cnt += abs(k) 
        cnt2 += k + i
        break
    
print(int(2*min(cnt,cnt2)))     