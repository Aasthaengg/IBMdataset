def check(List):
    List.sort()
    List.reverse()
    if List[0]**2 == List[1]**2+List[2]**2:
        return "YES"
    else:
        return "NO"

N = input()
    
for i in range(N):
    list = map(int, raw_input().split())
    print check(list)