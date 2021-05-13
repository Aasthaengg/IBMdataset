n,k = map(int,input().split())
List = list(map(int,input().split()))
List.sort(reverse=True)
print(sum(List[:k]))