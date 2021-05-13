from typing import List

n = int(input())
numbers = list(map(int, input().split()))

count = 0

def halfen(i: int)->int:
    return i >> 1

def isAllEven(l: List[int])->bool:
    for i in l:
        if(i % 2 == 1 or i == 0):
            return False
    return True

while True:
    if not isAllEven(numbers):
        break
    numbers = list(map(halfen, numbers))
    count += 1

print(count)
