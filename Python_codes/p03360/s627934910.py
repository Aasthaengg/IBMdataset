List = sorted([int(i) for i in input().split(" ")],reverse=True)
K = int(input())
List[0] = List[0]*(2**K)
print(sum(List))