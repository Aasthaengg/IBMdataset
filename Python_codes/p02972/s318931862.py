#d
n = int(input())
a = list(map(int, input().split()))
ans = [0]*len(a)
for i in range(len(a),0,-1):
    if sum(ans[i-1::i])%2 != a[i-1]:
        ans[i-1] = 1
print(sum(ans))
if sum(ans) > 0:
    ans_n = [str(i+1) for i, x in enumerate(ans)  if x==1]
    ans_n=" ".join(ans_n)
    print(ans_n)