N = int(input())
A = list(map(int, input().split()))

if N == 0 and A[0] == 1:
    print(1)
    exit()
 
if A[0] != 0:
    print(-1)
    exit()

A.reverse()
max_list = [A[0]]
before_top = A[0]
for i in range(1, len(A)):
    max_list.append(before_top + A[i])
    before_top = max_list[i]
    
A.reverse()
max_list.reverse()
ans = 1
before_top = 1
for i in range(1, len(A)):
    if A[i] <= before_top*2:
        ans += min(before_top*2, max_list[i])
        before_top = min(before_top*2, max_list[i]) - A[i]
    else:
        print(-1)
        exit()
        
print(ans)