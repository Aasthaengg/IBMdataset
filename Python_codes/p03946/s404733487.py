#import heapq
n,t = map(int,input().split())
ai = [int(i) for i in input().split()]


#rev_ai = [ai[n-1]*(-1)]

ans = [0,0]

max_ai = ai[n-1]

#heapq.heapify(rev_ai)
#print(rev_ai)
for i in range(1,n):
    #print(ai[n-1-i])
    dif = max_ai - ai[n-1-i]
    if dif > ans[0]:
        ans = [dif,1]
    elif dif == ans[0]:
        ans[1] += 1
    #print(rev_ai[0])
    #heapq.heappush(rev_ai,ai[n-1-i]*(-1))
    max_ai = max(max_ai,ai[n-1-i])

print(ans[1])