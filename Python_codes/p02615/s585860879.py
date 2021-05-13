N = int(input())
List = list(map(int,input().split()))
List += List
List = sorted(List)[::-1]
List = List[1:N]
print(sum(List))