n, k = map(int,input().split())

l=set()

for i in range(k):
    input()
    l = l | set(map(int,input().split()))

print(n-len(l))