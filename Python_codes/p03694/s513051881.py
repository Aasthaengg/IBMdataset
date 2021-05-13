n = int(input())
line = list(map(int,input().split()))
line.sort(key=int)
print(line[-1] - line[0])