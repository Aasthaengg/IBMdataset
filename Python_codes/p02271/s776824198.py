from functools import lru_cache

num = int(input())
arr = list(map(int, input().split()))
question_nums = int(input())
questions = list(map(int, input().split()))

@lru_cache(maxsize=2**12)
def solve(index, total):
    if total == 0:
        return True
    if index == num:
        return False
    return solve(index+1, total - arr[index]) or solve(index+1, total)

for q in questions:
    if solve(0, q):
        print("yes")
    else:
        print("no")
