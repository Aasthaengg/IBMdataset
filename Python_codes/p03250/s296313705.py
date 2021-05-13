ABC = list(map(int,input().split()))
ABC.sort()
answer = ABC[2] * 10 + ABC[1] + ABC[0]
print(answer)