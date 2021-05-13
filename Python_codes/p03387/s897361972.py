abc = list(map(int, input().split()))
abc.sort()

diff = 2*abc[2] - abc[0] - abc[1]

if diff%2:
    ans = (diff+1)//2 + 1
else:
    ans = diff//2
print(ans)