from typing import List


N: int = int(input())
A = list(map(int, input().split()))  # type: List[int]

print(max(A) - min(A))
