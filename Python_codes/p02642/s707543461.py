N = int(input())
A = list(map(int, input().split()))

List = [0 for x in range(1000001)]
answer = 0

def main(a, List):
    if List[a] >= 1:
        List[a] = List[a] + 1
        return List
    else:
        for i in range(a, 1000001, a):
            List[i] = List[i] + 1
    return List

def Answer(A, List):
    answer = 0
    for a in A:
        if List[a] == 1:
            answer += 1
    return answer

for a in A:
    main(a, List)

print(Answer(A, List))