A, B, C = map(int, input().split())
ABC = sorted([A, B, C], reverse=True)
print(int(str(ABC[0]) + str(ABC[1])) + ABC[2])
