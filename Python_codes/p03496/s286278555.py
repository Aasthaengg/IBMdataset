n=int(input())
a = list(map(int, input().split()))

max_a=max(a)
min_a=min(a)
max_ind=a.index(max_a)
min_ind=a.index(min_a)

ans=[]
if abs(max_a) >= abs(min_a):
    ans.append([max_ind+1,1])
    ans.append([max_ind+1,1])

    for i in range(n-1):
        ans.append([i+1,i+2])
        ans.append([i+1,i+2])
else:
    ans.append([min_ind+1,n])
    ans.append([min_ind+1,n])

    for i in reversed(range(n-1)):
        ans.append([i+2,i+1])
        ans.append([i+2,i+1])

print(len(ans))
for a in ans:
    print(*a)