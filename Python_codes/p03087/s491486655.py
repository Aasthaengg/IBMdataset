n,q = map(int,input().split())
s = input()
lr = [0] * (n+1)

for i in range(n):
    lr[i+1] = lr[i]+(1 if s[i:i+2] == "AC" else 0)

for i in range(q):
    st,fn = map(int,input().split())
    print(lr[fn-1] - lr[st-1])