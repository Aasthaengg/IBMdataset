N,K=map(int,input().split())

X=(N//K)**3

if K%2==0:
    X+=((N+K//2)//K)**3
print(X)