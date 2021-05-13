n=int(input())
t,a = map(int, input().split())
h= list(map(int, input().strip().split()))
for i in range(n):
    h[i]=abs(1000*t-6*h[i]-1000*a)
for i in range(n):
    if h[i]==min(h):
        print(i+1)