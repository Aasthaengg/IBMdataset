n=int(input())
a=list(map(int,input().split()))

a.sort()
import bisect
ans=0
#A=[1,2,3,4,5] #ソート済み
#index = bisect.bisect_left(A, 3) #2 同じ数字があった場合、前側の挿入箇所が返ってきている
#index = bisect.bisect_right(A, 3) # 3 同じ数字があった場合、後ろ側の挿入箇所が返ってきている
#A.insert(index, 3) #挿入
#print(a)
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        #a[i]<a[j]

        #a[k]<a[i]<a[j]

        #a[k]+a[i]>a[j]
        #=>a[i]> a[k] >a[j]-a[i]

        ll= bisect.bisect_right(a, a[j]-a[i])

        rr= bisect.bisect_left(a, a[i])
        if a[rr+1]==a[i]:
            rr=i
        #print(a[i],a[j],"|",ll,rr,max(0,rr-ll))
        ans+=(max(0,rr-ll))

print(ans)


