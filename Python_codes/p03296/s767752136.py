n = int(input())
li_a = list(map(int, input().split()))

prev = -1
answer = 0
for a in li_a:
    if prev == a:
        answer += 1
        prev = -1
    else:
        prev = a
print(answer)
