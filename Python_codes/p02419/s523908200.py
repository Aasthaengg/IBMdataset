# coding: utf-8
k_word = input()
count = 0

while True:
    s = input()
    
    if s == "END_OF_TEXT":
        break
    
    count += s.lower().split().count(k_word)

print(count)