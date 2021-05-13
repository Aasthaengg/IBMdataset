import collections

N = int(input())
A = map(int, input().split())
answer = 'YES'
for v in collections.Counter(A).values():
    if v != 1:
        answer = 'NO'
        break
print(answer)
