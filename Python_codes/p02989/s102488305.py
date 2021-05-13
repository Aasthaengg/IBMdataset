N=int(input())
List = list(map(int, input().split()))

List.sort()
divideNum=N//2
print(List[divideNum] - List[divideNum-1])