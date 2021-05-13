A,B,C = map(int,input().split())
K = int(input())
counter = 0
while A >= B:
    B *= 2
    counter += 1
while B >= C:
    C *= 2
    counter += 1
if counter <= K:
    print('Yes')
else:
    print('No')