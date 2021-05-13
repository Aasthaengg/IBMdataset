D = [[[0 for V in range(10)] for F in range(3)] for B in range(4)]

n = int(input())

for i in range(n):
    b,f,r,v = map(int,input().split())
    D[b-1][f-1][r-1] += v

for B in D[:-1]:
    for F in B:
        print(' ' + ' '.join(map(str,F)))
    print('#'*20)
for F in D[-1]:
    print(' ' + ' '.join(map(str,F)))