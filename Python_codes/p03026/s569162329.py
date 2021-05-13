#%%
n = int(input())
a, b = [0] * (n-1), [0] * (n-1)
reach = [[] for _ in range(n)]
for i in range(n-1):
    a[i], b[i] = map(int, input().split())
    reach[a[i]-1].append(b[i]-1)
    reach[b[i]-1].append(a[i]-1)
c = list(map(int, input().split()))
c.sort(reverse=True)
ans_list = [0] * n
check = [0] * n

stack = [0]
j = 0

while len(stack) > 0: 
    tmp = stack.pop(-1)
    check[tmp] = 1
    ans_list[tmp] = str(c[j])
    j += 1
    for i in range(len(reach[tmp])):
        if check[reach[tmp][i]] == 0:
            stack.append(reach[tmp][i])
        else:
            pass
    
print(sum(c) - max(c))
print(' '.join(ans_list))
