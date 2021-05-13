A,B,K = map(int, input().split())
 
 

 
 
ans = []
for x in range(A, min(A+K,B+1)):
    ans.append(x)
for x in range(max(A,B-K+1), B+1):
    ans.append(x)
for x in sorted(list(set(ans))):
    print(x)