k,x = map(int,input().split())
start = x - k + 1
end = x + k - 1
ans = ''
for i in range(start,end+1):
    ans += str(i) + ' '
print(ans[:len(ans)-1])
