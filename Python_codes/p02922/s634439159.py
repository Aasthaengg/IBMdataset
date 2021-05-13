s = list(map(int, input().split()))
a = s[0]
b = s[1]

outlet = 1
answer = 0

while(outlet < b):
    outlet -= 1
    outlet += a
    answer += 1

print(answer)