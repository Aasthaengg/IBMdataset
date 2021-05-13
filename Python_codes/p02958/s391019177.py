N = int(input())
list= list(map(int, input().split()))
newlist=list.copy()
c = 0
for all in range(N):
    if list[all]!=all+1:
        c+=1
if c == 0 or c ==2:
    print('YES')
else:
    print('NO')
