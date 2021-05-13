import bisect

N = int(input())
A = sorted(list(map(int,input().split())))
B = list(map(int,input().split()))
C = sorted(list(map(int,input().split())))

ans = 0
#print(A)
#print(C)
for b in B:
    lenA = bisect.bisect_left(A,b)
    lenC = N - bisect.bisect(C,b)
    ans += lenA*lenC
    #print(lenA,lenC)
    
print(ans)