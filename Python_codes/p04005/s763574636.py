ABC = list(map(int, input().split()))
ABC.sort()
if any(x % 2 == 0 for x in ABC):
    print(0)
else:
    print(ABC[0] * ABC[1])
