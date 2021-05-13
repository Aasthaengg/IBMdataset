#39 C - When I hit my pocket...
K,A,B = map(int,input().split())

if B <= A:
    ans = K + 1
else:
    nock = A - 1 + 2
    lest = K - nock
    ans = B + (lest//2)*(B-A) + (lest%2)*1
    ans = max(K+1,ans)
print(ans)