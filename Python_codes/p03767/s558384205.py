from collections import deque

n = int(input())
A = deque(sorted(map(int, input().split())))

def I_forgot_my_friends_birthday_sorry():
    for _ in range(n):
        A.popleft()
        A.pop()
        yield A.pop()

print(sum(I_forgot_my_friends_birthday_sorry()))