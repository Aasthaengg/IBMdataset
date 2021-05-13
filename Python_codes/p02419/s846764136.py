word = raw_input().lower()
total = 0
while True:
    str_list = raw_input().split(" ")
    
    if str_list[0] == "END_OF_TEXT":
       break
    
    for s in str_list:
        if s.lower() == word:
            total += 1

print total