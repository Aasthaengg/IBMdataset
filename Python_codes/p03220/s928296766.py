N = int(input())
T, A = list(map(lambda a: int(a), input().split(" ")))
dif = [abs(T - x * 0.006 - A) for x in list(map(lambda y: int(y), input().split(" ")))]
print(dif.index(min(dif)) + 1)