N = int(input())
count = 0
for i in range(N):
    l,r = map(int,input().split())
    if r>l:
        count += r-l+1
    else:
        count += 1 
print(count)