N = int(input())

an = list(map(int, input().split()))

#mã®åæå¤
result = 0
for a in an:
    result += (a -1)

print(result)
