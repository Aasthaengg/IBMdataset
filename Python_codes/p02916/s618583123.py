N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

now = 0
next = 0
ans = 0

for i in range(N):#ループ１ 0 ~ 2
    now = a[i]
    ans = ans + b[a[i]-1]
    
    if(i  < N-1):

        if(a[i + 1] == a[i] + 1):
            ans = ans + c[a[i]-1]
    
    

print(ans)

