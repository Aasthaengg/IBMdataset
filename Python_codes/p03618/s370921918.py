#D問題
A = list(str(input()))
N = len(A)

used = []
count = 0
for a in A:
    if a not in used:
        used.append(a)
        c = A.count(a)
        count+=(c*(c-1)//2)
            
ans = 1
for i in range(N):
    if i == 0:
        pass
    else:
        ans+=(N-i)
#print(ans,count)
ans-=count
print(ans)
