N = int(input())
li = list(map(int, input().split()))
an = 0
ma = 0
for i in range(N):
    if i != N-1 and li[i] >= li[i+1] :
        an += 1
    else:
        an = 0
    ma = max(an,ma)
print(ma)