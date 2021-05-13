n,m = list(map(int, input().split()))
h = list(map(int, input().split()))
nice = list(1 for i in range(n))
def chk_nice(x,y): 
    global nice
    if nice[x] != 0:
        nice[x] = (h[x] > h[y])
for i in range(m):
    a,b = list(map(int, input().split()))
    chk_nice(a-1, b-1)
    chk_nice(b-1, a-1)
print(sum(nice))

