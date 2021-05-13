# input
N = int(input())
S = set(map(str, input().split()))

# check
if len(S) == 3:
    print("Three")
else:
    print("Four")