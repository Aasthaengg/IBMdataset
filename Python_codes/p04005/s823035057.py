ABC = sorted(map(int, input().split()))
if not all(x % 2 for x in ABC):
    print(0)
else:
    print(ABC[0] * ABC[1])
