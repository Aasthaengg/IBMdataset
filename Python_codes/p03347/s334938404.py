#N, *a = map(int, open(0).read().split())
N = int(input())
a=[]
for i in range(N):
    a.append(int(input()))

def main():
    flag = 0
    tmp = a[-1]
    ans = 0
    
    for aa in reversed(a[:-1]):
        if aa >= tmp:
            ans += tmp
            tmp = aa
        elif aa +1 == tmp:
            ans += 1
            tmp = aa
        else:
            return -1

    if a[0] != 0:
        ans = -1
    return ans
            
print(main())
