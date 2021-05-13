N, K = map(int, input().split())
A=list(map(int, input().split()))

num=0
while num*K-(num-1)<N:
    num+=1
print(num)