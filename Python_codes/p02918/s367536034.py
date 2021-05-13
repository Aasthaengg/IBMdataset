n, k = map(int, input().split())
s = str(input())

start = s[0]
end = s[-1]

count = 0
flag = 0
answer = 0
for i in range(1,n):
    if s[i-1] == start and s[i] != start and flag == 0:
        flag += 1
    elif s[i-1] != start and s[i] == start and flag == 1:
        flag = 0
        count += 1
    if s[i-1] == s[i]:
        answer += 1
#%%
answer += min(count,k)*2
if k > count:
    answer += flag

print(answer)