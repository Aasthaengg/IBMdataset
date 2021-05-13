ABC = list(map(int, input().split()))

ABC.sort(reverse=True)

print(int(''.join(map(str, ABC[:2]))) + int(ABC[-1]))