n = int(input())
a = set(map(int, input().split()))
kinds = len(a)
if kinds % 2 == 1:
    print(kinds)
else:
    print(kinds - 1)