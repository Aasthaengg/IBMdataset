import sys

n = input()
x = list(map(int,input().split()))
ans = sys.maxsize

# i = min(x)
# while i <= max(x):
for i in range(min(x),max(x)+1,1):
    tmp = sum(map(lambda p: (p-i)**2,x))
    if ans > tmp:
        ans = tmp
    # i += 1
print(ans)