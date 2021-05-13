n = int(input())
S = [x for x in input().split()]
q = int(input())
T = [x for x in input().split()]
answer = {x for x in S if x in T}
print(len(answer))