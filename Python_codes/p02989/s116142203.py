n = int(input())
D = sorted(list(map(int, input().split())))

print(D[len(D)//2]-D[len(D)//2-1])