word = input().lower()
cnt = 0
while True:
    text = input()
    if text == "END_OF_TEXT": break
    text_list = list(text.split())
    for i in text_list:
        if i.lower() == word:
            cnt += 1
print(cnt)