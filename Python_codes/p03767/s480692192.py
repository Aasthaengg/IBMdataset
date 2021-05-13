N = int(input())
INT_LIST_SORETED = sorted([int(s) for s in input().split()], reverse=True)
SECOND_INT_LIST_MAX = [val for idx, val in enumerate(INT_LIST_SORETED)
                       if idx <= 2 * N and idx % 2 == 1]
print(sum(SECOND_INT_LIST_MAX))
