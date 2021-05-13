List = [int(input()) for _ in range(4)]
Train = min(List[:2])
Bus = min(List[2:])
print(Train+Bus)