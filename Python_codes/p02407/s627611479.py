n = int(input())
v = list(map(int, input().split()))
w = v[::-1]
print((' ').join(map(str,w)))