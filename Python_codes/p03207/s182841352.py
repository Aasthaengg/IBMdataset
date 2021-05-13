N = int(input())
List = [int(input()) for _ in range(N)]
last = sorted(List)[-1] * 0.5
print(int(sum(List) - last))