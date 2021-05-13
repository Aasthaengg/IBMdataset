N,K = map(int, input().split())
H = list(map(int, input().split()))

temp = sorted(H,reverse=True)
new_H = temp[K:len(temp)]

if(N-K<=0):
    print(0)
else:
    print(sum(new_H))


