H,N = map(int, input().split())
lists = list(map(int, input().split()))
lists.sort()
SAM = sum(lists)
if SAM>=H:
    print('Yes')
else:
    print('No')
