a, b, c = map(int,input().split())
bell = [a, b, c]
bell.sort()
answer = bell[0] + bell[1]
print(answer)
