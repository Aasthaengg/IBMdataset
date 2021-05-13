#template
def inputlist(): return [int(k) for k in input().split()]
#template
A = inputlist()
A.sort(reverse=True)
ans = 0
for i in range(1,3):
    ans += A[i-1]-A[i]
print(ans)