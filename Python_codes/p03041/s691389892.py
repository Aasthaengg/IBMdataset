n, k = map(int, input().split())
s = str(input())
answer = ''

for i in range(n):
    string = s[i]
    if i == k - 1:
        string = string.lower()

    answer += string

print(answer)