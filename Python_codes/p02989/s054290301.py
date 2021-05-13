n=int(input())
List=list(map(int,input().split()))
List.sort()
print(List[len(List)//2]-List[len(List)//2-1])