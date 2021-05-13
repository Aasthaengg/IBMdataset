import bisect
n,k = map(int,input().split())
a = list(map(int,input().split()))
# for i in a[0:bisect.bisect_left(t,0)]:
m = a[0:bisect.bisect_left(a,0)]+[0]
p = [0]+a[bisect.bisect_left(a,0):]
# for i in range(len(m)-2,-1,-1):
#     m[i] += m[i+1]
# for i in range(1,len(p)):
#     p[i] += p[i-1]
# print(p)
# print(m)
ans = 10**9
for i in range(max(k-len(m)+1,0),min(len(p),k+1)):
    ans = min(ans,2*p[i]+abs(m[-(k-i+1)]))
    # print(ans,i,-(k-i+1),p[i],abs(m[-(k-i)]))
for i in range(max(k-len(p)+1,0),min(len(m),k)):
    ans = min(ans,2*abs(m[-i-1])+abs(p[k-i]))
    # print(ans,i,(k-i),abs(m[-i-1]),abs(p[k-i]))
print(ans)