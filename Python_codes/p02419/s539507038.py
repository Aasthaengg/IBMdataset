word = input().upper()
ans = 0
while True:
    sent = input()
    if sent == 'END_OF_TEXT':
        break
    ans += sent.upper().split().count(word)
print(ans)
