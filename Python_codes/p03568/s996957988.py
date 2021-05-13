n = int(input())
A = list(map(int,input().split()))

odd_pair = 1
all_pair = 1
for a in A:
    all_pair*=3
    if a%2==0:
        odd_pair*=2
print(all_pair-odd_pair)