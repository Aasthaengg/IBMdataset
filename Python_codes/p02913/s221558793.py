N = int(input())
S = input()
 
r = 0
ans = 0
for l in range(N):
 
    while True:
        #print(S.rfind(S[l:r+1]), S[l:r+1], l, r)
 
        if S.rfind(S[l:r+1]) >= r+1:
            r += 1
            ans = max(ans, r-l)
        else:
            break
 
print(ans)
