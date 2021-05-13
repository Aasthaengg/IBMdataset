N ,K= map(int, input().split())
List = list(map(int, input().split()))
List.sort(reverse=True)
if N<=K:
    print(0)
else:
    new=List[K:]
    print(sum(new))