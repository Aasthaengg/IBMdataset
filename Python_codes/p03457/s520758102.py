N = int(input())
t = [list(map(int,input().split())) for _ in range(N)]
x,k,y = 0,0,0
for i in range(N):
    if (abs(t[i][1] - x) + abs(t[i][2] - y) > t[i][0] - k 
       or (abs(t[i][1] - x) + abs(t[i][2] - y))%2 != (t[i][0] - k)%2):
       print("No")
       exit()
    x = t[i][1]
    y = t[i][2]
    k = t[i][0]
print("Yes")