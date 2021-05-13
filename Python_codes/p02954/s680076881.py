S = list(input())
N = len(S)
start = 0
end = 0
ans = [0]*N

for i in range(1,N):
    if S[i-1] == S[i]:
        continue
    elif S[i-1] == 'R' and S[i] == 'L':
        r = i-1
        l = i

    elif S[i-1] == 'L' and S[i] == 'R':
        end = i-1

        ans[r] = int((r-start+2)/2) + int((end-l+1)/2)
        ans[l] = int((end-l+2)/2) + int((r-start+1)/2)
        start = i

end = N-1
ans[r] = int((r-start+2)/2) + int((end-l+1)/2)
ans[l] = int((end-l+2)/2) + int((r-start+1)/2)

for a in ans:
    print(a, end=' ')
print("")