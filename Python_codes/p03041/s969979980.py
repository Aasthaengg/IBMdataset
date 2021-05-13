N , K= list(map(int,input().split()))
S = input()

after=str.lower(S[K-1])

ans = S[:K-1] + after + S[K:]
print(ans)