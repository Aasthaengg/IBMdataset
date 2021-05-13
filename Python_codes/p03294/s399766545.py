N = int(input())

an = list(map(int, input().split()))

#mの初期値
result = 0
for a in an:
    result += (a -1)

print(result)
