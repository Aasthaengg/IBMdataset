a,b,n = list(map(int, input().split()))
def f(x):
    return a*x//b - a*(x//b)

left=1
right=n
for _ in range(100):
    delta=(right-left)/3
    midl=left+delta
    midr=midl+delta
#    print(f'left={left} midl={midl} midr={midr} right={right}')
    if f(midl)>f(midr):
        right=midr
    else:
        left=midl
print(max(f(int(midl)),f(min(int(midl)+1,n))))